from stats import get_num_words, generate_sorted_dictionary
from collections import Counter
import sys

file_name=""
try:
    file_name = sys.argv[1]
except:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

file_countent, number_of_words = get_num_words(file_name)
all_char_string = "".join(file_countent).lower()
char_count = Counter(all_char_string)

# give this to the function to generate the sorted dictionary in the list
char_count_list = generate_sorted_dictionary(char_count)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {number_of_words} total words")
print("--------- Character Count -------")

for char in char_count_list:
    if char['character'].isalpha():
        print(f"{char['character']}: {char['count']}")

print("============= END ===============")
