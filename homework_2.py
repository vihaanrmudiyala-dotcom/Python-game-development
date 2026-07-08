students = {}

while True:
    print("\nStudent Grade Menu")
    print("1. Add student grade")
    print("2. View all grades")
    print("3. Search student grade")
    print("4. Update student grade")
    print("5. Delete student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print("Student grade added.")

    elif choice == "2":
        if students:
            print("\nAll Student Grades:")
            for name, grade in students.items():
                print(name, ":", grade)
        else:
            print("No students found.")

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print(name, "has grade", students[name])
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")

    elif choice == "5":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")