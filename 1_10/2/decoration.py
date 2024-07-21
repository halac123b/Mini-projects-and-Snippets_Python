# importing libraries
import time
import math


#### Sample 1: Decoration void function ####
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
# Tự động gọi hàm calculate_time() với factorial() được pass là 1 arg
factorial(10)


#### Sample 2: Decoration that return a value ####
def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        # Hàm con cần nhận tham số dưới dạng general (*args, **kwargs), khi đó có thể pass vào bất kỳ hàm nào
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))


#### Sample 3: Chaining decorator, các hàm decorator có thể lồng nhau ####
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())
