class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student1):
        if len(self.students) < self.max_students:
            self.students.append(student1)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for stu in self.students:
            value += stu.get_grade()
        return value/len(self.students)


student = [['rabin', 22, 95], ['sabin', 1, 75], ['ram', 19, 65]]
course = Course('Science', 2)
for i in student:
    s = Student(i[0], i[1], i[2])
    print(course.add_student(s))


print(course.get_average_grade())




