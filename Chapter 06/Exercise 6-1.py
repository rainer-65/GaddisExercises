# Programming Exercise 6-1

def main():
    # Declare local variables
    contents = ''

    try:
        # Open numbers.txt file for reading
        infile = open('numbers.txt', 'r')

        # Option 1: Easiest solution
        for line in infile:
            print(line.strip())

        # Option 2: Using built-in readlines()
        # contents = infile.readlines()
        # for item in contents:
        #     print(item.strip())
        # Close file
        # infile.close()

        # Option 3: Using built-in readline()
        # line = infile.readline()
        # while line:
        #   print(line.strip())
        #   line = infile.readline()
        # infile.close()

    except Exception:
        print("IO Error occurred")


# Call the main function.
if __name__ == '__main__':
    main()
