from unittest import TestCase
from lexnlp.extract.common.dates_classifier_model import get_date_features
from lexnlp.extract.de.date_model import DE_ALPHA_CHAR_SET, DATE_MODEL_CHARS


class TestDateClassifierModel(TestCase):
    def test_get_word_tokens(self):
        text = 'Leasing mit 2.500€ Anzahlung: Monatliche Rate 230,55€'
        features = get_date_features(text, 0, len(text),
                                     characters=DATE_MODEL_CHARS,
                                     norm=False,
                                     count_words=True,
                                     alphabet_char_set=DE_ALPHA_CHAR_SET)
        self.assertEqual(1, features['nb31'])
        self.assertEqual(3, features['na31'])
        self.assertEqual(1, features['wr_l'])
        self.assertEqual(4, features['wr_u'])
