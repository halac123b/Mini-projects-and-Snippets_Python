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


#### Sample 3: Return 1 hàm dưới dạng 1 hàm khác ####
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))
