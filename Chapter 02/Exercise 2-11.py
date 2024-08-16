# Programming Exercise 2-11

# Variables for the number of male and female students,
# total number of students, and the percentage of male
# and female students.
male = 0
female = 0
total = 0
percentMale = 0.0
percentFemale = 0.0

# Get the number of male students.
male = int(input('Enter the number of male students: '))

# Get the number of female students.
female = int(input('Enter the number of female students: '))

# Calculate the total number of students.
total = male + female

# Calculate the percentage of male students.
percentMale = male / total

# Calculate the percentage of female students.
percentFemale = female / total

# Print the percentage of male students.
print(f'Male: {percentMale:.2%}')

# Print the percentage of female students.
print(f'Male: {percentFemale:.2%}')
