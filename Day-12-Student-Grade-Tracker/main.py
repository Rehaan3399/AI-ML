  import json
  import csv
  students = {}
  # Add Student
  def add_student():
      name = input("Enter student name: ")
      marks = int(input("Enter marks: "))
      students[name] = marks
      print("Student added successfully!")
  # View Students
  def view_students():
      if not students:
          print("No students found.")
          return
      print("\nStudent Records")
      for name, marks in students.items():
          print(f"{name}: {marks}")
  # Save to JSON
  def save_json():
      with open("students.json", "w") as file:
          json.dump(students, file, indent=4)
      print("Data saved to JSON successfully!")
  # Load from JSON
  def load_json():
      global students
      try:
          with open("students.json", "r") as file:
              students = json.load(file)
          print("Data loaded successfully!")
      except FileNotFoundError:
          print("No JSON file found.")
  # Export to CSV
  def export_csv():
      with open("students.csv", "w", newline="") as file:
          writer = csv.writer(file)
  
          writer.writerow(["Name", "Marks"])
  
          for name, marks in students.items():
              writer.writerow([name, marks])
      print("Data exported to CSV!")
  # Menu
  while True:
      print("\n===== STUDENT GRADE TRACKER =====")
      print("1. Add Student")
      print("2. View Students")
      print("3. Save to JSON")
      print("4. Load from JSON")
      print("5. Export to CSV")
      print("6. Exit")
      choice = input("Enter choice: ")
      if choice == "1":
          add_student()
      elif choice == "2":
          view_students()
      elif choice == "3":
          save_json()
      elif choice == "4":
          load_json()
  
      elif choice == "5":
          export_csv()
      elif choice == "6":
          print("Goodbye!")
          break
      else:
          print("Invalid choice!")
