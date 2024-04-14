def count_word_occurrences(text):
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_word_counts(word_counts):
    max_word_length = max(len(word) for word in word_counts)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


user_input = input("Enter a string: ")
occurrences = count_word_occurrences(user_input)
print_word_counts(occurrences)