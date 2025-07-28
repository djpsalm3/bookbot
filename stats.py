from collections import defaultdict

def word_count(file_contents):
    words = file_contents.split()
    num_words = len(words)   
    return (f"Found {num_words} total words")

def character_count(file_contents):
    char_counts = defaultdict(int) 
    for char in file_contents:
        lower_char = char.lower() 
        char_counts[lower_char] += 1 
    return dict(char_counts)  

def sorted_dictionary(character_counts_dict: dict[str, int]) -> list[dict[str, int]]:
    list_of_dicts = [{'char': char, 'num': count} for char, count in character_counts_dict.items() if char.isalpha()]
    list_of_dicts.sort(key=lambda x: x['num'], reverse=True)
    return list_of_dicts


#[item for item in iterable if condition]