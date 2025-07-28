import sys
from stats import word_count
from stats import character_count
from stats import sorted_dictionary

if len(sys.argv) < 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return (file_contents)
char_frequency = character_count

def main():
    text = get_book_text(sys.argv[1])
    char_counts_dict = char_frequency(text)
    #print(word_count(text))
    #print(char_counts_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(word_count(text))
    print("--------- Character Count -------")
    #print(sorted_dictionary(char_counts_dict))
    for item in sorted_dictionary(char_counts_dict):
        print(f"{item['char']}: {item['num']}")            
    print("============= END ===============")
main()