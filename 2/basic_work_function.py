#### Sample 1: Pass function as variable ####


def shout(text):
    return text.upper()


print(shout("Hello"))

# Gán reference của hàm cho biến
yell = shout

print(yell("Hello"))


#### Sample 2: Pass function là 1 arg của hàm khác ####
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


# Gọi hàm với 2 tham số hàm khác nhau
greet(shout)
greet(whisper)
