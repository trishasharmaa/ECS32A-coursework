import re
from collections import Counter
from typing import List, Tuple


def c_word(word: str) -> str:
    """Removes leading and trailing special characters from a word and converts it to lowercase.

    Args:
        word: The word to clean.

    Returns:
        The cleaned, lowercase word.
    """
    return re.sub(r"^[,.:;\"|\\!@#$%^&*()_+\-=\[\]{}<>?/~`']+|[,.:;\"|\\!@#$%^&*()_+\-=\[\]{}<>?/~`']+$", "", word).lower()


def read_words(file_path: str) -> List[str]:
    """Reads words from a file and processes them to remove special characters and convert to lowercase.

    Args:
        file_path: The path to the file containing the words.

    Returns:
        A list of cleaned words from the file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        w = re.findall(r'\S+', text)
        return [c_word(word) for word in w]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []


def filter_words(w: List[str], ignore_str: List[str]) -> List[str]:
    """Filters out the ignored words from the list of words.

    Args:
        w: The list of words to filter.
        ignore_str: The list of words to ignore.

    Returns:
        The filtered list of words.
    """
    return [word for word in w if word not in ignore_str]


def n_words(w: List[str], n: int) -> List[Tuple[str, int]]:
    """Gets the top N most occurring words along with their counts.

    Args:
        w: The list of words to analyze.
        n: The number of top occurring words to display.

    Returns:
        A list of tuples containing the top N words and their counts.
    """
    word_count = Counter(w)
    common_word = word_count.most_common()
    top_word = []
    current_count = 0

    for word, count in common_word:
        if len(top_word) < n:
            current_count = count
            top_word.append((word, count))
        elif count == current_count:
            top_word.append((word, count))
        else:
            break

    return top_word


def main():
    """Main function to execute the program."""
    file_path = input("Enter the name of the file: ").strip()
    n = int(input("Enter how many top words you want to see: ").strip())

    w = read_words(file_path)
    if not w:
        return

    ignore_str = ['a', 'an', 'and', 'in', 'is', 'the']
    filtered_word = filter_words(w, ignore_str)

    top_word = n_words(filtered_word, n)

    if not top_word:
        print("No words to display.")
        return

    current_count = top_word[0][1]
    current_word = []

    for word, count in top_word:
        if count == current_count:
            current_word.append(word)
        else:
            print(f"The following words appeared {current_count} times each: {', '.join(current_word)}")
            current_count = count
            current_word = [word]

    if current_word:
        print(f"The following words appeared {current_count} times each: {', '.join(current_word)}")


if __name__ == "__main__":
    main()
