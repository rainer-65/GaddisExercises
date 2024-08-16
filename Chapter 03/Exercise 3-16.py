year = int(input("Enter a year: "))
message = ""

if year > 0:
    # Valid
    message = "In " + format(year) + " February has "

    if year % 100 == 0:
        # Might be leap
        if year % 400 == 0:
            message += "29"
        else:
            message += "28"
    else:
        # Might be leap
        if year % 4 == 0:
            message += "29"
        else:
            message += "28"

    message += " days."

else:
    # Invalid
    message = "Enter a year greater that 0\n" + \
              "Rerun the program and try again."

print(message)
