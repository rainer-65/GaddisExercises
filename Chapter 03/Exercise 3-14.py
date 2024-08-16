# Programming Exercise 3-14

# Local variables
weight = 0.0
height = 0.0
BMI = 0.0

# Get the weight from the user.
weight = float(input('Enter your weight in kilo: '))

# Get the height from the user.
height = float(input('Enter your height in meter: '))

# Calculate the body mass.
BMI = weight / (height * height)

# Display BMI.
print(f'Your Body Mass Indicator is {BMI:.2f}')

# Determine and display weight category.
if BMI > 25:
    print('You are overweight.')
elif BMI < 18.5:
    print('You are underweight.')
else:
    print('Your weight is optimal.')