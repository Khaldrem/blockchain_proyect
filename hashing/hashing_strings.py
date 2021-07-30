import hashlib

#Expect bytes as inputs
input_as_bytes = b"Hola soy un string!"
first_output = hashlib.sha256(input_as_bytes)

#Only H to h changed
input_as_bytes_changed = b"hola soy un string!"
second_output = hashlib.sha256(input_as_bytes_changed)

print(f"First input: {input_as_bytes}")
print(first_output.hexdigest())
print("##############################")

print(f"Second input: {input_as_bytes_changed}")
print(second_output.hexdigest())
print("##############################")

print(f"Are the same?: {first_output.hexdigest() == second_output.hexdigest()}")