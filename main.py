def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_number = get_words_number(text)
    char_count_dict = count_char(text.lower())
    char_data_list = statistics(char_count_dict)
    print_data(book_path,words_number,char_data_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_words_number(text):
    return len(text.split())

def count_char(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            if(char not in char_dict):
                char_dict[char] = 1
            elif(char in char_dict):
                char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def statistics(char_count_dict):
    temp_list = []
    for item in char_count_dict:
        temp_dict = {}
        temp_dict["name"] = item
        temp_dict["num"] = char_count_dict[item]
        temp_list.append(temp_dict)
    temp_list.sort(reverse=True,key=sort_on)
    return temp_list

def print_data(book_path,words_number,char_data_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_number} words found in the document\n")
    for item in char_data_list:
        print(f"The '{item['name']}' character was found {item['num']} times")
    print("--- End report ---")

if __name__ == '__main__':
    main()