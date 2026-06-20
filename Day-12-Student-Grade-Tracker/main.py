import json
students = {}
while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Save Data")
    print("4.Load Data")
    print("5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
    elif choice == "2":
        print(students)
    elif choice == "3":
        with open("students.json", "w") as f:
            json.dump(students, f)
        print("Data Saved")
    elif choice == "4":
        with open("students.json", "r") as f:
            students = json.load(f)
        print(students)
    elif choice == "5":
        break
