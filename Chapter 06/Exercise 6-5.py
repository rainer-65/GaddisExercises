# Programming Exercise 6-5

infile = None


def main():
    # Open the text infile for reading

    global infile
    try:
        infile = open("numbers.txt", 'r')
        # Initialize a variable to store the sum
        total_sum = 0

        # Read each line from the infile and convert to integers
        for line in infile:
            number = int(line.strip())  # Convert the line to an integer
            total_sum += number  # Add the integer to the sum

    except ValueError:
        print("Value Error occurred")
    except IOError:
        print("IO Error occurred")
    except Exception:
        print("An error occurred:")
    else:
        # Print the sum
        print("Sum of integers:", total_sum)
    finally:
        infile.close()


# Call the main function.
if __name__ == '__main__':
    main()
