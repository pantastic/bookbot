def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    text = file_contents
    words = file_contents.split()
    word_count = len(words)
    characters = count_letters(text)
    create_report(word_count, characters, book_path)

def count_letters(text):
    characters = {}

    for c in text:
        c_lower = c.lower() 
        if c_lower in characters:
            characters[c_lower] += 1
        else:
            characters[c_lower] = 1
    return(characters)

def sort_text(characters):
    char_dict_list = []
    for character in characters:
        if character.isalpha():
            new_dict = {
                "character": character,
                "count": characters[character]
            }
            char_dict_list.append(new_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

def sort_on(dict):
    return dict["count"]
  

def create_report(word_count, characters, path):
    char_sorted = sort_text(characters)
    
    print(f"---==>> Printing a report of {path} <<==---")
    print(f"it contains {word_count} words, wow!")

    for character in char_sorted:
        print(f"the letter {character['character']} appears {character['count']} times")
    
    print(f"---==>> That's it, all done <<==---")

def convert(dictionary):
  return [{key: value} for key, value in dictionary.items()]


main()
