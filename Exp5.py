num_students = int(input("Enter number of students in class:"))
class_total = 0
for student in range(1,num_students + 1):

    print("\Enter score for student {student}:")

    student_total = 0

    for test in range(1,6):
        score = float(input(f"Enter score for Test {test}:"))
        student_total += score

    student_avg = student_total/5

    print(f"Average score of Student{student}:{student_avg:.2f}")

    class_total += student_total

overall_avg = class_total/(num_students*5)

print(f"\nOverall average score of the class: {overall_avg:.2f}")