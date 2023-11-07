def initialize_character_count(string, alphabet_size=256):
    character_count = [0] * max(alphabet_size, len(string))
    for character in string:
        character_count[ord(character)] += 1
    return character_count

def cumulative_count(character_count):
    for i in range(1, len(character_count)):
        character_count[i] += character_count[i - 1]
    return character_count

def sort_initial_positions(string, character_count):
    string_length = len(string)
    positions = [0] * string_length
    for index in reversed(range(string_length)):
        character_count[ord(string[index])] -= 1
        positions[character_count[ord(string[index])]] = index
    return positions

def assign_character_classes(sorted_positions, string):
    string_length = len(string)
    classes = [0] * string_length
    number_of_classes = 1
    classes[sorted_positions[0]] = 0
    for i in range(1, string_length):
        if string[sorted_positions[i]] != string[sorted_positions[i - 1]]:
            number_of_classes += 1
        classes[sorted_positions[i]] = number_of_classes - 1
    return classes, number_of_classes

def sort_doubled_shifts(string, sorted_positions, character_classes, number_of_classes, shift_length):
    string_length = len(string)
    count = [0] * number_of_classes
    new_positions = [(position - (1 << shift_length)) % string_length for position in sorted_positions]
    for position in new_positions:
        count[character_classes[position]] += 1
    count = cumulative_count(count)
    for position in reversed(new_positions):
        count[character_classes[position]] -= 1
        sorted_positions[count[character_classes[position]]] = position
    return sorted_positions

def update_classes(sorted_positions, character_classes, shift_length):
    string_length = len(sorted_positions)
    new_classes = [0] * string_length
    number_of_classes = 1
    new_classes[sorted_positions[0]] = 0
    for i in range(1, string_length):
        current = (character_classes[sorted_positions[i]], character_classes[(sorted_positions[i] + (1 << shift_length)) % string_length])
        previous = (character_classes[sorted_positions[i - 1]], character_classes[(sorted_positions[i - 1] + (1 << shift_length)) % string_length])
        if current != previous:
            number_of_classes += 1
        new_classes[sorted_positions[i]] = number_of_classes - 1
    return new_classes, number_of_classes

def sort_cyclic_shifts(string):
    character_count = initialize_character_count(string)
    character_count = cumulative_count(character_count)
    initial_sorted_positions = sort_initial_positions(string, character_count)
    classes, number_of_classes = assign_character_classes(initial_sorted_positions, string)

    shift_length = 0
    while (1 << shift_length) < len(string):
        initial_sorted_positions = sort_doubled_shifts(string, initial_sorted_positions, classes, number_of_classes, shift_length)
        classes, number_of_classes = update_classes(initial_sorted_positions, classes, shift_length)
        shift_length += 1

    return initial_sorted_positions

def build_suffix_array(string_with_terminator):
    cyclic_shifts_sorted = sort_cyclic_shifts(string_with_terminator)
    return cyclic_shifts_sorted[1:]

def build_lcp_array(original_string, suffix_array):
    string_length = len(original_string)
    inverse_suffix_array = [0] * string_length
    lcp_array = [0] * (string_length - 1)

    for i, suffix in enumerate(suffix_array):
        inverse_suffix_array[suffix] = i

    common_prefix_length = 0
    for i in range(string_length):
        if inverse_suffix_array[i] == string_length - 1:
            common_prefix_length = 0
            continue

        next_suffix_index = suffix_array[inverse_suffix_array[i] + 1]
        while (i + common_prefix_length < string_length and
               next_suffix_index + common_prefix_length < string_length and
               original_string[i + common_prefix_length] == original_string[next_suffix_index + common_prefix_length]):
            common_prefix_length += 1

        lcp_array[inverse_suffix_array[i]] = common_prefix_length
        if common_prefix_length:
            common_prefix_length -= 1

    return lcp_array

def count_unique_repeated_substrings(input_string):
    string_with_terminator = input_string + "$"
    suffix_array = build_suffix_array(string_with_terminator)
    lcp_array = build_lcp_array(input_string, suffix_array)
    unique_repeated_substrings_count = sum(max(0, current_lcp - next_lcp) for current_lcp, next_lcp in zip(lcp_array, lcp_array[1:] + [0]))
    return unique_repeated_substrings_count

def main():
    number_of_cases = int(input())
    results = (count_unique_repeated_substrings(input().strip()) for _ in range(number_of_cases))
    print(*results, sep='\n')
    # Add comment so it registers my commit
main()
