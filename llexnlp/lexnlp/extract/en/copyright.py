"""Copyright extraction for English using NLTK and NLTK pre-trained maximum entropy classifier.

This module implements basic Copyright extraction functionality in English relying on the pre-trained
NLTK functionality, including POS tagger and NE (fuzzy) chunkers.

Todo: -
"""

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2021, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/2.1.0/LICENSE"
__version__ = "2.1.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"

import string
from typing import Generator, List, Tuple, Union

from lexnlp.extract.common.copyrights.copyright_en_style_parser import CopyrightEnStyleParser
from lexnlp.extract.common.annotations.copyright_annotation import CopyrightAnnotation
from lexnlp.extract.en.utils import NPExtractor


grammar = r"""
    NBAR:
        {<NNP.*|JJ|CD|NN|\(|\)|,>*<NNP.*|CD>}  # Nouns, Adj-s, brackets, terminated with Nouns/Numbers
    IN:
        {<CC|IN>}   # &, and, of
    NP:
        {(<NBAR><IN>)*<NBAR>}
"""


class CopyrightNPExtractor(NPExtractor):

    allowed_sym = ['&', 'and', 'of', '©']
    allowed_pos = ['IN', 'CC', 'NN']

    @staticmethod
    def strip_np(np):
        return np.strip(string.punctuation.replace('(', '') + string.whitespace)


np_extractor = CopyrightNPExtractor(grammar=grammar)


class CopyrightEnParser(CopyrightEnStyleParser):
    @classmethod
    def extract_phrases_with_coords(cls, sentence: str) -> List[Tuple[str, int, int]]:
        return np_extractor.get_np_with_coords(sentence)


def get_copyright(
    text: str,
    return_sources: bool = False
) -> Generator[Union[Tuple[str, str, str], Tuple[str, str, str, str]], None, None]:
    for ant in get_copyright_annotations(text, return_sources):
        if return_sources:
            yield ant.sign, ant.date, ant.name, ant.text
        else:
            yield ant.sign, ant.date, ant.name


def get_copyright_annotations(text: str, return_sources=False) -> \
        Generator[CopyrightAnnotation, None, None]:
    for ant in CopyrightEnParser.get_copyright_annotations(text,
                                                           return_sources):
        ant.locale = 'en'
        yield ant
