import string

banner = (
    "\n==============================================\n"
    " Welcome to the Word Completion Finder!\n"
    "==============================================\n"
    "This program helps you find words that begin\n"
    "with a given prefix from any text file you choose.\n"
    "Type '#' at any time to quit.\n"
)


def open_file():
    while True:
        try:
            filename = input("\n:~Input a file name ~:")
            fp = open(filename, "r", encoding='UTF-8')
            return fp
        except FileNotFoundError:
            print("[Error]: no such file")


def read_file(fp):
    word_set = set()
    try:
        for line in fp:
            words_list = line.split()
            for word in words_list:
                valid_word = word_process(word)
                if valid_word:
                    word_set.add(valid_word)
        print("\nYour vocabulary data file includes {} unique words.".format(len(word_set)))
    finally:
        fp.close()
    return word_set


def word_process(word):
    if "'" in word:
        return None
    clean_word = word.strip(string.punctuation).lower()
    if not clean_word.isalpha() or len(clean_word) < 2:
        return None
    return clean_word


def set_dictionary(word_set):
    dictionary = {}
    for word in word_set:
        for position, char in enumerate(word):
            key = (position, char)
            dictionary.setdefault(key, set()).add(word)
    return dictionary


def find_matches(prefix, dictionary):
    if not prefix:
        all_words = set()
        for word_set in dictionary.values():
            all_words.update(word_set)
        return all_words

    sets_match = []
    for position, char in enumerate(prefix):
        key = (position, char)
        if key not in dictionary:
            return set()
        sets_match.append(dictionary[key])

    results = sets_match[0].copy()
    for match in sets_match[1:]:
        results &= match
    if not results:
        return set()
    return results


def main():
    print(banner)
    fp = open_file()
    word_set = read_file(fp)
    word_set = set_dictionary(word_set)

    while True:
        prefix = input("\n:~Enter a prefix to search (# to quit) ~:")
        if prefix == '#':
            print("\nGood Bye")
            break
        else:
            completion_set = find_matches(prefix, word_set)
            if prefix == "" or not completion_set:
                print("There are no completions.")
            else:
                word_list = sorted(list(completion_set))
                word_list = ", ".join(map(str, word_list))
                print("The words that completes '{}' are: {}".format(prefix, word_list))


if __name__ == "__main__":
    main()
