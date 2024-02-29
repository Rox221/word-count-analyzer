def word_count_analyzer(text):
    # Convert text to lowercase to ensure case-insensitivity
    text = text.lower()
    
    # Split the text into words
    words = text.split()

    # Count the occurrences of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Print the word count results
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Example usage
sample_text = "This is a sample text. This text is just an example."
word_count_analyzer(sample_text)
