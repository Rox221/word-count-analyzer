## Word Count Analyzer
- word_count_analyzer is a function that takes a text input as an argument.

- text = text.lower(): It converts the entire text to lowercase, ensuring case-insensitivity in counting words.

- words = text.split(): It splits the lowercase text into a list of words. The default separator for split() is any whitespace character.(eg. space, tab, newline)

- word_count = {}: Initializes an empty dictionary to store the count of each word.

- Loop through each word in the list of words:

if word in word_count: checks if the word is already in the dictionary.
If yes, increment the count for that word by 1 (word_count[word] += 1).
If not, add the word to the dictionary with a count of 1 (word_count[word] = 1).

- Use a Python dictionary (word_count) to store the count of each unique word and show which words show up the most.
