import weakref

class MyClass:
    pass

# Create an object and a weak reference to it
obj = MyClass()
weak_ref = weakref.ref(obj)

# Print the object and the weak reference
print(obj)       # Prints the object instance
print(weak_ref())  # Prints the same object instance

# Delete the original reference
del obj

# Try to print obj
print(obj)       # This will raise a NameError: name 'obj' is not defined

# Print the weak reference
print(weak_ref())  # This will print None, because the object has been garbage-collected