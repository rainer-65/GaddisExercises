def main():
    # Receive user input
    full_name = input('Enter your full name: ')
    # Split according to spaces
    name = full_name.split()

    # The first character of each name is an initial
    for string in name:
        print(string[0].upper(), sep='', end='')
        print('.', sep=' ', end='')


# Call the main function.
main()
