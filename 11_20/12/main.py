import hashlib

input_data_byte = bytes(5)

# Create SHA-256 hash object from input byte
hash_object = hashlib.sha256(input_data_byte)

# Present hash object as string in hexadecimal
hex_dig = hash_object.hexdigest()
