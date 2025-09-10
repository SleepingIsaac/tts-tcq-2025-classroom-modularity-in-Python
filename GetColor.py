MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

NUMBER_OF_MAJOR_COLORS = len(MAJOR_COLORS)
NUMBER_OF_MINOR_COLORS = len(MINOR_COLORS)


def get_color_from_pair_number(pair_number):
    #Get color pair based on pair number."""
    pair_number -= 1  # Convert to zero-based index
    major_color = pair_number // NUMBER_OF_MINOR_COLORS
    minor_color = pair_number % NUMBER_OF_MINOR_COLORS
    return MAJOR_COLORS[major_color], MINOR_COLORS[minor_color]

def get_pair_number_from_color(major_color, minor_color):
    #Get pair number based on major and minor colors."""
    major_index = MAJOR_COLORS.index(major_color)
    minor_index = MINOR_COLORS.index(minor_color)
    return major_index * NUMBER_OF_MINOR_COLORS + minor_index + 1

def get_color_code_mapping():
    #Provides the entire color code mapping in a formatted printable form. Returns a list of strings.
    formatted_mapping = []
    for pair_number in range(1, NUMBER_OF_MAJOR_COLORS * NUMBER_OF_MINOR_COLORS + 1):
        major, minor = get_color_from_pair_number(pair_number)
        formatted_mapping.append(f"Pair Number: {pair_number}, Major: {major}, Minor: {minor}")
    return formatted_mapping