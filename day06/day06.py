from utils.utils import read_file


def string_has_duplicate_chars(string_to_test):
    for ch in string_to_test:
        if string_to_test.count(ch) > 1:
            return True
    return False


def get_first_unique_string_index(string_to_search, search_len):
    start = -1
    end = search_len
    while end < len(string_to_search):
        start += 1
        end = start + search_len
        s = string_to_search[start:end]
        if not string_has_duplicate_chars(s):
            return end
    return -1


def main():
    data = read_file("data.dat")
    for row in data:
        idx = get_first_unique_string_index(row, 4)
        print("Start of packet marker... ", end='')
        if idx >= 0:
            print(f"pos {idx}")
        else:
            print("No marker!")

        idx = get_first_unique_string_index(row, 14)
        print("Start of message marker... ", end='')
        if idx >= 0:
            print(f"pos {idx}")
        else:
            print("No marker!")


if __name__ == "__main__":
    main()
