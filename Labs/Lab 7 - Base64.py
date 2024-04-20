"""
Import the Base64 library. 
Get a secret from the user. 
Encode and print the secret. 
Decode and print the secret

"""
import base64

# Get secret from user
secret = input("Enter your secret message: ")

# Encode the secret
encoded_secret = base64.b64encode(secret.encode("utf-8")).decode("utf-8")
print(f"Encoded Secret: {encoded_secret}")

# Decode the secret
decoded_secret = base64.b64decode(encoded_secret.encode("utf-8")).decode("utf-8")
print(f"Decoded Secret: {decoded_secret}")