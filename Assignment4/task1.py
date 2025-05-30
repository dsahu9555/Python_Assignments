try:
    with open("sample.txt", 'r') as file:
        reading = file.readlines()
        count = 1
        for line in reading:
            print(f"Line {count}: {line}")
            count += 1
except FileNotFoundError:
    print(f"The file \'sample.txt\' was not found.")
