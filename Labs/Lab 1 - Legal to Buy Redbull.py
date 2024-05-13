"""
Ask the User for their Age.
Perform casting to convert Step 1 to int from str. 
Create an if-else statement to verify the age: ex 18 
Print result to User if they are allowed or not to buy


""" 


# Step 1 and 2
age = int(input("How old are you? "))
# step 3 and 4
if age >= 18:
  print("You are an adult so you can drink.")
elif age >= 15:
   print("you can buy redbull")
else:
    print("You are a minor so you can’t drink.")



