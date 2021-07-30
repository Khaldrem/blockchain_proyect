from hashlib import sha256

file = open("./images/cat_test.jpg", "rb")
hash = sha256(file.read()).hexdigest()
file.close()

print(f"The hash of the file is: {hash}")