students = {
    "Raj": 85,
    "Mac": 65,
    "Sam": 88
}
name = input("Enter the student's name: ")
if name in students:
    print("{}'s marks: {}".format(name, students[name]))
else:
    print("Student not found.")
