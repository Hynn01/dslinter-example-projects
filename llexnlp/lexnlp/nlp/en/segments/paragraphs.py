"""Paragraph segmentation for English.

This module implements paragraph segmentation in English using simple
machine learning classifiers.

Todo:
  * Standardize model (re-)generation
"""

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2021, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/2.1.0/LICENSE"
__version__ = "2.1.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"

import os
# Imports
import re
import string
import unicodedata
from typing import Generator, List, Tuple, Union, Optional

# Packages
import pandas
import joblib

from lexnlp.nlp.en.segments.utils import build_document_line_distribution


# Setup module path
MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

# Load segmenters
PARAGRAPH_SEGMENTER_MODEL = joblib.load(os.path.join(MODULE_PATH, "./paragraph_segmenter.pickle"))


def build_paragraph_break_features(lines: List[str],
                                   line_id: int,
                                   line_window_pre: int,
                                   line_window_post: int,
                                   characters=string.printable,
                                   include_doc=None):
    """
    Build a feature vector for a given line ID with given parameters.
    """
    # Feature vector
    feature_vector = {}

    # Check start offset
    if line_id < line_window_pre:
        line_window_pre = line_id

    # Check final offset
    if (line_id + line_window_post) >= len(lines):
        line_window_post = len(lines) - line_window_post - 1

    # Iterate through window
    for i in range(-line_window_pre, line_window_post + 1):
        try:
            line = lines[line_id + i]
        except IndexError:
            continue

        # Count length
        feature_vector["line_len_{0}".format(i)] = len(line)
        feature_vector["line_lenstrip_{0}".format(i)] = len(line.strip())
        feature_vector["line_title_case_{0}".format(i)] = line == line.title()
        feature_vector["line_upper_case_{0}".format(i)] = line == line.upper()

        # Count characters
        feature_vector["line_n_alpha_{0}".format(i)] = sum([1 for c in line if unicodedata.category(c).startswith("L")])
        feature_vector["line_n_number_{0}".format(i)] = sum(
            [1 for c in line if unicodedata.category(c).startswith("N")])
        feature_vector["line_n_punct_{0}".format(i)] = sum([1 for c in line if unicodedata.category(c).startswith("P")])
        feature_vector["line_n_whitespace_{0}".format(i)] = sum(
            [1 for c in line if unicodedata.category(c).startswith("Z")])

    # Simple checks
    line = lines[line_id]
    feature_vector["first_char_punct"] = (line.strip()[0] in string.punctuation) if len(line.strip()) > 0 else False
    feature_vector["last_char_punct"] = (line.strip()[-1] in string.punctuation) if len(line.strip()) > 0 else False
    feature_vector["first_char_number"] = (line.strip()[0] in string.digits) if len(line.strip()) > 0 else False
    feature_vector["last_char_number"] = (line.strip()[-1] in string.digits) if len(line.strip()) > 0 else False

    # Build character vector
    for character in characters:
        feature_vector["char_{0}".format(character)] = lines[line_id].count(character)

    # Add doc if requested
    if include_doc:
        feature_vector.update(include_doc)

    return feature_vector


def get_paragraph_break_feature_names(
        lines_count: int,
        line_window_pre: int,
        line_window_post: int,
        characters=string.printable,
        include_doc=None):
    """
    Build a feature vector for a given line ID with given parameters.
    """
    # Feature vector
    feature_vector = {
        'first_char_punct',
        'last_char_punct',
        'first_char_number',
        'last_char_number'
    }

    # Check start offset
    if lines_count - 1 < line_window_pre:
        line_window_pre = lines_count - 1

    # Check final offset
    if line_window_post >= lines_count:
        line_window_post = lines_count - line_window_post - 1

    # Iterate through window
    for i in range(-line_window_pre, line_window_post + 1):

        # Count length
        feature_vector.add(f'line_len_{i}')
        feature_vector.add(f'line_lenstrip_{i}')
        feature_vector.add(f'line_title_case_{i}')
        feature_vector.add(f'line_upper_case_{i}')
        # Count characters
        feature_vector.add(f'line_n_alpha_{i}')
        feature_vector.add(f'line_n_number_{i}')
        feature_vector.add(f'line_n_punct_{i}')
        feature_vector.add(f'line_n_whitespace_{i}')

    # Build character vector
    for character in characters:
        feature_vector.add(f"char_{character}")

    # Add doc if requested
    if include_doc:
        feature_vector.update(set(include_doc.keys()))

    return feature_vector


RE_NEW_LINE = re.compile(r'(?P<line>[^\r\n]*)((\r\n)|(\n\r)|\n|\r)')


def splitlines_with_spans(text: str) -> Tuple[List[str], List[Tuple[int, int]]]:
    lines: List[str] = []
    spans: List[Tuple[int, int]] = []
    if text is None:
        return lines, spans
    last_line_end = -1
    for m in RE_NEW_LINE.finditer(text):
        line = m.group('line')
        span = m.span()
        lines.append(line)
        spans.append(span)
        last_line_end = span[1]
    if last_line_end < len(text):
        lines.append(text[last_line_end:len(text)])
        spans.append((last_line_end, len(text)))
    return lines, spans


def _maybe_paragraph(pos0: int, pos1: Optional[int], text: str, line_spans: List[Tuple[int, int]], return_spans: bool) \
        -> Optional[Union[str, Tuple[str, int, int]]]:
    span = (line_spans[pos0][0], line_spans[pos1][0] if pos1 is not None else len(text))
    paragraph = text[span[0]:span[1]]

    if len(paragraph.strip()) > 0:
        if return_spans:
            return paragraph, span[0], span[1]
        return paragraph


def get_paragraphs(text: str, window_pre=3, window_post=3,
                   score_threshold=0.5, return_spans: bool = False) -> Generator:
    """
    Get paragraphs.
    """
    # Get document character distribution
    doc_distribution = build_document_line_distribution(text)
    lines, line_spans = splitlines_with_spans(text)
    feature_data = []

    for line_id in range(len(lines)):
        feature_data.append(
            build_paragraph_break_features(lines, line_id, window_pre, window_post,
                                           include_doc=doc_distribution))

    # Predict page breaks
    column_names = list(get_paragraph_break_feature_names(
        len(lines), window_pre, window_post, include_doc=doc_distribution))
    column_names.sort()
    feature_df = pandas.DataFrame(feature_data, columns=column_names).fillna(-1).astype(int)
    try:
        predicted_lines = PARAGRAPH_SEGMENTER_MODEL.predict_proba(feature_df)
        predicted_df = pandas.DataFrame(predicted_lines, columns=["prob_false", "prob_true"])
        paragraph_breaks = predicted_df.loc[predicted_df["prob_true"] >= score_threshold, :].index.tolist()

        if len(paragraph_breaks) > 0:
            # Get first break
            pos0 = 0
            pos1 = paragraph_breaks[0]

            maybe_paragraph = _maybe_paragraph(pos0, pos1, text, line_spans, return_spans)
            if maybe_paragraph is not None:
                yield maybe_paragraph

            # Iterate through section breaks
            for i in range(len(paragraph_breaks) - 1):
                # Get breaks
                pos0 = paragraph_breaks[i]
                pos1 = paragraph_breaks[i + 1]
                # Get text
                maybe_paragraph = _maybe_paragraph(pos0, pos1, text, line_spans, return_spans)
                if maybe_paragraph is not None:
                    yield maybe_paragraph

            # Yield final section
            pos0 = paragraph_breaks[-1]
            pos1 = None
            maybe_paragraph = _maybe_paragraph(pos0, pos1, text, line_spans, return_spans)
            if maybe_paragraph is not None:
                yield maybe_paragraph
        else:
            yield (text, 0, len(text)) if return_spans else text
    except ValueError as e:
        if 'Number of features of the model must match the input' in str(e):
            yield (text, 0, len(text)) if return_spans else text
        else:
            raise e
