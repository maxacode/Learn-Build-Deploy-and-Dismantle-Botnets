"""
Lab 5: Infinite Files
Create a file while using error handling. 
Create a try block. 
Create a loop to write text to the file from users input
Break the loop if the word exit is entered. 

"""

try:
  # Open the file in append mode ('a') for adding user input
  with open("my_file.txt", "a") as file:
    while True:
      # Get user input
      text = input("Enter text to write (type 'exit' to stop): ")

      # Check for exit condition
      if text.lower() == "exit":
        break

      # Write text to the file
      file.write(text + "\n")  # Add newline character for each line

  print("Text successfully written to the file!")
except Exception as e:
  print("An error occurred:", e)