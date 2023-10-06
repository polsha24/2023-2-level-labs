"""
Checks the second lab's load vocabulary function
"""

import unittest
from pathlib import Path

import pytest

from lab_2_tokenize_by_bpe.main import load_vocabulary


class LoadVocabularyTest(unittest.TestCase):
    """
    Tests loading vocabulary function
    """
    def setUp(self) -> None:
        self.vocabulary_path = str(Path(__file__).parent / 'vocabulary.json')
        self.path_to_invalid_vocabulary = str(Path(__file__).parent / 'invalid_vocabulary.json')

    @pytest.mark.lab_2_tokenize_by_bpe
    @pytest.mark.mark10
    def test_load_vocabulary_ideal(self):
        """
        Ideal load vocabulary scenario
        """
        expected = {"альбатро": 0, "ных</s>": 1, "что</s>": 2, "го</s>": 3, "ет</s>": 4,
                    "их</s>": 5, "ли</s>": 6, "ми</s>": 7, "на</s>": 8, "не</s>": 9,
                    "но</s>": 10, "ся</s>": 11, "то</s>": 12, "ют</s>": 13, ",</s>": 14,
                    ".</s>": 15, "<unk>": 16, "а</s>": 17, "в</s>": 18, "е</s>": 19,
                    "и</s>": 20, "й</s>": 21, "к</s>": 22, "м</s>": 23, "о</s>": 24,
                    "с</s>": 25, "т</s>": 26, "у</s>": 27, "х</s>": 28, "ы</s>": 29,
                    "ь</s>": 30, "ю</s>": 31, "я</s>": 32, "—</s>": 33, "</s>": 34,
                    "птиц": 35, "аль": 36, "ени": 37, "мер": 38, "мно": 39, "при": 40,
                    "про": 41, "пти": 42, "ско": 43, "ста": 44, "сто": 45, "тен": 46,
                    "ат": 47, "бо": 48, "ва": 49, "ви": 50, "во": 51, "вы": 52, "го": 53,
                    "да": 54, "де": 55, "до": 56, "ду": 57, "ен": 58, "ер": 59, "ет": 60,
                    "за": 61, "из": 62, "ин": 63, "ит": 64, "ка": 65, "ки": 66, "ко": 67,
                    "ла": 68, "ле": 69, "ли": 70, "ло": 71, "ль": 72, "ми": 73, "мо": 74,
                    "на": 75, "не": 76, "ни": 77, "но": 78, "ны": 79, "об": 80, "од": 81,
                    "он": 82, "по": 83, "ра": 84, "ре": 85, "ри": 86, "ро": 87, "ру": 88,
                    "ры": 89, "се": 90, "си": 91, "со": 92, "ст": 93, "те": 94, "ти": 95,
                    "то": 96, "ча": 97, "че": 98, "ше": 99, "!": 100, "(": 101, ")": 102,
                    "*": 103, ",": 104, "-": 105, ".": 106, "/": 107, "0": 108, "1": 109,
                    "2": 110, "3": 111, "4": 112, "5": 113, "6": 114, "7": 115, "8": 116,
                    "9": 117, ":": 118, ";": 119, "<": 120, ">": 121, "?": 122, "A": 123,
                    "D": 124, "O": 125, "P": 126, "S": 127, "X": 128, "a": 129, "c": 130,
                    "d": 131, "e": 132, "i": 133, "l": 134, "m": 135, "n": 136, "o": 137,
                    "r": 138, "s": 139, "t": 140, "y": 141, "«": 142, "»": 143, "А": 144,
                    "Б": 145, "В": 146, "Г": 147, "Д": 148, "Е": 149, "Ж": 150, "З": 151,
                    "И": 152, "К": 153, "Л": 154, "М": 155, "Н": 156, "О": 157, "П": 158,
                    "Р": 159, "С": 160, "Т": 161, "У": 162, "Ф": 163, "Х": 164, "Ч": 165,
                    "Ш": 166, "Э": 167, "Я": 168, "а": 169, "б": 170, "в": 171, "г": 172,
                    "д": 173, "е": 174, "ж": 175, "з": 176, "и": 177, "й": 178, "к": 179,
                    "л": 180, "м": 181, "н": 182, "о": 183, "п": 184, "р": 185, "с": 186,
                    "т": 187, "у": 188, "ф": 189, "х": 190, "ц": 191, "ч": 192, "ш": 193,
                    "щ": 194, "ъ": 195, "ы": 196, "ь": 197, "э": 198, "ю": 199, "я": 200,
                    "–": 201, "—": 202, "…": 203}
        actual = load_vocabulary(self.vocabulary_path)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_tokenize_by_bpe
    @pytest.mark.mark10
    def test_load_vocabulary_internal_type(self):
        """
        Load vocabulary invalid internal type
        """
        expected = None
        actual = load_vocabulary(self.path_to_invalid_vocabulary)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_tokenize_by_bpe
    @pytest.mark.mark10
    def test_load_vocabulary_bad_input(self):
        """
        Load vocabulary invalid inputs check
        """
        bad_inputs = [{}, (), None, 1, 1.1, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = load_vocabulary(bad_input)
            self.assertEqual(expected, actual)

    @pytest.mark.lab_2_tokenize_by_bpe
    @pytest.mark.mark10
    def test_load_vocabulary_return_value(self):
        """
        Load vocabulary return value check
        """
        actual = load_vocabulary(self.vocabulary_path)
        self.assertTrue(isinstance(actual, dict))
        for key in actual:
            self.assertTrue(isinstance(actual[key], int))
            self.assertTrue(isinstance(key, str))
