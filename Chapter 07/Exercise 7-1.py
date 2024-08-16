def calculate():
    sales = []
    total = 0
    for i in range(7):
        sale = input(f"Enter the sales for day {i + 1}: ")
        sales.append(sale)
        total += float(sale)
    print(f"The total sales for the week is: {total}")


# Call the function
calculate()
