import textwrap

#  Loại bỏ space thừa ở đầu dòng và cuối dòng
print(textwrap.dedent(f"""
    Line 1
    Line 2
        Line 3
""").strip())