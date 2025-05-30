with open("output.txt", 'w') as file:
    string = input("Enter text to write to the file: ")
    file.write(string)
    print("Data successfully written to output.txt.")

with open("output.txt", 'a') as file:
    string = input("Enter additional text to append: ")
    file.write("\n"+ string)
    print("Data successfully appended.")

with open("output.txt", 'r+') as file:
    data = file.read()
    print(data)
