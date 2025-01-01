from cryptography.fernet import Fernet

# Put this somewhere safe!
# Fernet là 1 implementation of symmetric (also known as “secret key”) authenticated cryptography
key = Fernet.generate_key()
fernetObject = Fernet(key)
# Mã hoá 1 string, return token là dữ liệu đã bị mã hoá
token = fernetObject.encrypt(b"A really secret message. Not for prying eyes.")

fernetObject.decrypt(token)