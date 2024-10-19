"""
CP1404: Practical 5
Word occurrences

Estimate: 25 minutes
Actual:   35 minutes
"""

# Dictionary to store word counts
word_to_count = {}

# Get input from user
text = input("Text: ")

# Split the text into words
words = text.split()

# Count the occurrences of each word
for word in words:
    # Use the get method to handle missing keys
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# Sort the words alphabetically
sorted_words = sorted(word_to_count.keys())

# Find the length of the longest word for formatting
max_length = max(len(word) for word in sorted_words)

# Print the words and their counts, formatted with alignment
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
