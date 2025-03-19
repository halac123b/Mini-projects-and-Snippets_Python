def getFortunes():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()  # Removes newline characters
    return lines