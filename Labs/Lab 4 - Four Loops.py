"""
Create an iteration of four loops. 
Ask the user for a number every time
Multiply all the numbers
Handle potential errors. 

"""
 
product = 1  # Initialize product to 1 for multiplication

for _ in range(4):  # Loop four times using throwaway variable "_"
  while True:  # Loop for valid input
    try:
      number = float(input("Enter a number: "))
      product *= number  # Multiply the product by the current number
      break  # Exit the inner loop if input is valid
    except ValueError:
      print("Invalid input. Please enter a number.")

print(f"The product of all numbers is: {product}")