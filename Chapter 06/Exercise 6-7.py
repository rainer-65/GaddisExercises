# Programming Exercise 6-7

import random


def main():
    # Local variables
    filename = ''
    numberOfRandoms = 0
    randomNumber = 0

    # Get the file name as input from the user.
    filename = input('Enter the name of the file to '
                     'which results should be written: ')

    # Get the number of items to write to the file.
    numberOfRandoms = int(input('Enter the number of '
                                'random numbers to be '
                                'written to the file: '))

    # Open output file.
    outputFile = open(filename, 'w')

    # Write specified number of random numbers to the file.
    for counter in range(numberOfRandoms):
        randomNumber = random.randint(1, 500)
        outputFile.write(str(randomNumber) + '\n')

    # Close the file.
    outputFile.close()


# Call the main function.
if __name__ == '__main__':
    main()
