def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()

    num_words = count_words(file_contents)

    print(f"--- Report of {book_path} ---")
    print(f"{num_words} found in the book")

    chars = char_count(file_contents)

    letter_count = convert_dicts(chars)

    print(letter_count)


def count_words(book):
    words = book.split()
    num_words = len(words)

    return num_words


def char_count(book):
    letter_count = {}
    for char in book:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    return letter_count


def convert_dicts(input_dict):
    output_list = []
    for item in input_dict:
        if item.isalpha():
            to_add = {"character": item, "num": input_dict[item]}
            output_list.append(to_add)

    return output_list


def sort_on(dict):
    return dict["num"]


main()
