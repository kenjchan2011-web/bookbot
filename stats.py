
def get_book_text( path_to_file ):

    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()

    return file_contents

def get_num_words(file_path):
    #file_content = get_book_text('books/frankenstein.txt')
    file_content = get_book_text(file_path)
    word_count = len(file_content.split())

    return file_content, word_count

# Add a new function to your stats.py file that takes the dictionary of characters 
# and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself 
# and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Use the .sort() method:
# Use a helper function to return the "num" key of each dictionary for comparison.
# Sort the list from greatest to least by the count.

def generate_sorted_dictionary(counter):
    # Iterate over the key-value pairs
    list_of_dictionaries = [{'character': key, 'count': value} for key, value in counter.items()]
    list_of_dictionaries.sort(key=lambda d: d['count'], reverse=True)
    
    return list_of_dictionaries 
