# file handling

# Region 1
# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')
# End region 1

# Region 2
# A custom resource class, phải gồm 2 hàm __enter__() và __exit__()
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, *args):
        self.file.close()

# using with statement with MessageWriter
with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')
# End region