"""
Language detection starter
"""
from lab_1_classify_by_unigrams.main import tokenize, calculate_frequencies, create_language_profile, detect_language


def main() -> None:
    """
    Launches an implementation
    """
    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()
    unk = create_language_profile("unk", unknown_text)
    en = create_language_profile("en", en_text)
    de = create_language_profile("de", de_text)
    result = detect_language(unk, en, de)
    assert result, "Detection result is None"


if __name__ == "__main__":
    main()