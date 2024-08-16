# Programming Exercise 9-4

def main():
    # Get name of input file.
    input_name = input('Enter the name of the input file: ')

    # Open the input file and read the text.

    # Remove punctuation
    all_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    input_file = open(input_name, 'r')
    text = input_file.read()
    for elements in text:
        if elements in all_punct:
            text = text.replace(elements, "")

    words = text.split()
    # List comprehension for enabling sorting of set entries
    words = [word.lower() for word in words]

    # Create set of unique words.
    unique_words = set(words)

    # Print the results.
    print('These are the unique words in the text:')
    unique_words = sorted(unique_words)
    for word in unique_words:
        print(word)

    # Close the file.
    input_file.close()


# Call the main function.
if __name__ == '__main__':
    main()
