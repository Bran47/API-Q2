class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def get_average_grade(self, subject=None):
        if subject:
            if subject in self.grades:
                grades = self.grades[subject]
                return sum(grades) / len(grades)
            else:
                return None  # or handle this case as per your requirements
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            if all_grades:
                return sum(all_grades) / len(all_grades)
            else:
                return None  # or handle this case as per your requirements
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Student Name: {student.name}")
            print("Grades:")
            for subject, grades in student.grades.items():
                print(f"{subject}: {grades}")

    def get_student_average_grade(self, student_name, subject= all):
        for student in self.students:
            if student.name == student_name:
                return student.get_average_grade(subject)
        return None  # or handle this case as per your requirements

    def get_class_average_subject(self, subject):
        total_grades = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total_grades += sum(student.grades[subject])
                count += len(student.grades[subject])
        if count > 0:
            return total_grades / count
        else:
            return None  # or handle this case as per your requirements

    def get_class_average_all_subjects(self):
        total_grades = 0
        count = 0
        for student in self.students:
            average_grade = student.get_average_grade()
            if average_grade is not None:
                total_grades += average_grade
                count += 1
        if count > 0:
            return total_grades / count
        else:
            return None  # or handle this case as per your requirements

# Create a Classroom instance
classroom = Classroom()

# Add some students
student1 = Student("Brandon")
student1.add_grade("Programming", 75)
student1.add_grade("Ethics", 65)
classroom.add_student(student1)

student2 = Student("Brian")
student2.add_grade("Programming", 70)
student2.add_grade("Ethics", 67)
classroom.add_student(student2)

student3 = Student("Kingsley")
student3.add_grade("Programming", 77)
student3.add_grade("Ethics", 62)
classroom.add_student(student3)

# Display all students and their grades
print("All Students:")
classroom.display_students()

# Get class average for a subject
subject = "programming"
subject = "ethics"
class_average = classroom.get_class_average_subject(subject)
if class_average:
    print(f"\nClass average in {subject}: {class_average}")
else:
    print(f"\nNo students have grades in {subject}")

# Get average grade of a student across all subjects
student_name = "Brandon"
average_grade_all_subjects = classroom.get_student_average_grade(student_name)
if average_grade_all_subjects:
    print(f"\nAverage grade of {student_name} across all subjects: {average_grade_all_subjects}")
else:
    print(f"\n{student_name} not found or has no grades in any subjects")

# Get class average across all subjects
class_average_all_subjects = classroom.get_class_average_all_subjects()
if class_average_all_subjects:
    print(f"\nClass average across all subjects: {class_average_all_subjects}")
else:
    print(f"\nNo students have grades in any subjects")
