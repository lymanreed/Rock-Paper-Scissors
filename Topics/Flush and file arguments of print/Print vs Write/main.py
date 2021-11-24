numbers = [1234, 5678, 90]
filename = "file_with_list.txt"
with open(filename, "w") as f:
    print(numbers, end="", file=f)
