marks = {}

# Ask the user to enter 5 subjects and their marks
for i in range(5):
    subject = input(f"Enter subject {i + 1}: ")
    mark = float(input(f"Enter marks for {subject}: "))
    marks[subject] = mark

# Find total and average marks
total_marks = sum(marks.values())
average_marks = total_marks / len(marks)

print("\nMarks Dictionary:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)