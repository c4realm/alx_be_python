#understanding the question, use for loop to generate and print the multiplication table for a given number, enter a number, then use a for loop to print multiplication table for that number from 1 to 10.

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")


