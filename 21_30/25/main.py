import multiprocessing


def print_cube(num):
    """function to print cube of given num"""
    print(f"Cube: {num * num * num}")


def print_square(num):
    """function to print square of given num"""
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # starting process, khá tương tự thread
    p1.start()
    p2.start()

    print(p1.pid)  # Process id
    print(p1.is_alive())  # bool, check xem process còn chạy k

    # Dừng chương trình chính đợi process chạy xong (giống thread)
    p1.join()
    p2.join()
