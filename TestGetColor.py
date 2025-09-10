from GetColor.py import get_color_from_pair_number, get_pair_number_from_color, get_color_code_mapping


def test_number_to_pair(pair_number, expected_major, expected_minor):
    major, minor = get_color_from_pair_number(pair_number)
    print(f"Got pair: {major} {minor}")
    assert major == expected_major, "Major color mismatch!"
    assert minor == expected_minor, "Minor color mismatch!"


def test_pair_to_number(major, minor, expected_pair_number):
    pair_number = get_pair_number_from_color(major, minor)
    print(f"Got pair number: {pair_number}")
    assert pair_number == expected_pair_number, "Pair number mismatch!"

def test_color_code_mapping():
    print("\nComplete Color Code Mapping:")
    mapping = get_color_code_mapping()
    for line in mapping:
        print(line)

if __name__ == "__main__":
    # Test cases
    test_number_to_pair(4, "White", "Brown")
    test_number_to_pair(5, "White", "Slate")
    test_pair_to_number("Black", "Orange", 12)
    test_pair_to_number("Violet", "Slate", 25)