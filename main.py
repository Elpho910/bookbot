def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()

    num_words = count_words(file_contents)

    print(f"--- Report of {book_path} ---")
    print(f"{num_words} words found in the book")

    chars = char_count(file_contents)

    letter_count = convert_dicts(chars)
    letter_count.sort(key=sort_on, reverse=True)
    # print(letter_count)

    for item in letter_count:
        character = item["character"]
        num = item["num"]
        print(f"The '{character}' character was found {num} times")


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
