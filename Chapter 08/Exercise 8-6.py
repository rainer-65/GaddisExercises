# Programming Exercise 8-6

def main():
    # Local variables
    num_sentences = 0
    total_words = 0
    average_words = 0.0
    words = []

    try:
        # Open file text.txt for reading.
        infile = open('text.txt', 'r')

        # Read data into a list.
        # Each list item is one sentence.
        sentences = infile.readlines()

        # The number of sentences is equal to
        # the length of the list.
        num_sentences = len(sentences)

        # The number of items in each list 
        # is the number of words in the sentence.
        for item in sentences:
            words = item.split()
            total_words += len(words)

        # Calculate average words.
        average_words = float(total_words) / num_sentences

        # Display average words.
        print (f'Average number of words per line: {average_words}')

        # Close the file.
        infile.close()

    # Handle any errors that may occur.
    except IOError:
        print('There was an error while opening the file.')
    except:
        print('An error occurred.')

# Call the main function.
if __name__ == '__main__':
    main()