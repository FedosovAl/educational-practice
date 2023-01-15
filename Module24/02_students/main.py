# TODO здесь писать код

class Student:

    def __init__(self, name, number, marks):
        self.name_and_surname = name
        self.number_group = number
        self.student_performance = marks.split()

    def find_arithmetic_mean(self):
        total = 0
        for element in self.student_performance:
            total += int(element)
        score = total / 5
        return score


class Rating:
    def sorted_students(self, student_arithmetic_mean):
        new_student_arithmetic_mean = dict()
        sort_arithmetic_mean = sorted(student_arithmetic_mean.values())
        sort_arithmetic_mean = sort_arithmetic_mean[::-1]
        for element in sort_arithmetic_mean:
            for name, score in student_arithmetic_mean.items():
                if element == score:
                    new_student_arithmetic_mean[name] = element
        return new_student_arithmetic_mean

    def creating_and_recording_rating(self, all_students, student_arithmetic_mean):
        with open('rating.txt', 'w', encoding='utf-8') as rating:
            for name_and_surname in student_arithmetic_mean.keys():
                for name, group, marks in all_students:
                    if name_and_surname == name:
                        rating.write(name + '' + group + '' + marks + '\n')


students = []
arithmetic_mean = dict()
with open('students.txt', 'r', encoding='utf-8') as students_data:
    for student in students_data:
        student = student.rstrip()
        student = student.split(',')
        students.append(student)
for student_name, group_number, student_marks in students:
    result = Student(student_name, group_number, student_marks)
    arithmetic_mean[student_name] = result.find_arithmetic_mean()
result = Rating()
new_arithmetic_mean = result.sorted_students(arithmetic_mean)
result.creating_and_recording_rating(students, new_arithmetic_mean)
