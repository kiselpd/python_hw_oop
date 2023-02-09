class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def has_course_attached(self, course):
        return course in self.courses_attached


class Lecturer(Mentor):

    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __average_rating(self):
        count_marks = 0
        sum_marks = 0

        for key in self.grades:
            count_marks += len(self.grades[key])
            sum_marks += sum(self.grades[key])

        return round(sum_marks / count_marks, 3) if count_marks != 0 else 0

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_rating()}"

    def __lt__(self, other):
        return self.__average_rating() < other.__average_rating()

    def __gt__(self, other):
        return self.__average_rating() > other.__average_rating()

    def __eq__(self, other):
        return self.__average_rating() == other.__average_rating()


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def has_finished_course(self, course):
        return course in self.finished_courses

    def has_course_in_progress(self, course):
        return course in self.courses_in_progress

    def rate_lecturer(self, course, lecturer: Lecturer, grade: list):
        if not lecturer.has_course_attached(course):
            print("Лектор не ведет такой курс(%s)" % (course))
            return

        if not self.has_course_in_progress(course) and not self.has_finished_course(course):
            print("Студент не занимался на этих курсах(%s)" % (course))
            return

        if course in lecturer.grades:
            lecturer.grades[course] += grade
        else:
            lecturer.grades[course] = grade

    def __average_rating(self):
        count_marks = 0
        sum_marks = 0

        for key in self.grades:
            count_marks += len(self.grades[key])
            sum_marks += sum(self.grades[key])

        return round(sum_marks / count_marks, 3) if count_marks != 0 else 0

    def __str__(self):
        out_str = f"\nИмя: {self.name}\nФамилия: {self.surname}\n"
        out_str += f"Средняя оценка за домашние задания: {self.__average_rating()}\n"
        out_str += f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        out_str += f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return out_str

    def __lt__(self, other):
        return self.__average_rating() < other.__average_rating()

    def __gt__(self, other):
        return self.__average_rating() > other.__average_rating()

    def __eq__(self, other):
        return self.__average_rating() == other.__average_rating()


class Reviewer(Mentor):

    def rate_hw(self, student: Student, course, grade):
        if student.has_course_in_progress(course):
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            print("Студент не занимается на этом курсе(%s)" % (course))

    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}"


def average_rating_students(students: list, course):
    count_marks = 0
    sum_marks = 0
    for student in students:
        if course in student.grades and isinstance(student, Student):
            sum_marks += sum(student.grades[course])
            count_marks += len(student.grades[course])
    
    return round(sum_marks / count_marks, 3) if count_marks != 0 else 0


def average_rating_lecturers(lecturers: list, course):
    count_marks = 0
    sum_marks = 0
    for lecturer in lecturers:
        if course in lecturer.grades and isinstance(lecturer, Lecturer):
            sum_marks += sum(lecturer.grades[course])
            count_marks += len(lecturer.grades[course])
    
    return round(sum_marks / count_marks, 3) if count_marks != 0 else 0

#testing classes and methods
def solution():
    student1 = Student("Павел", "Киселев", "мужчина")
    student1.finished_courses = ["django", "git"]
    student1.courses_in_progress = ["c++", "python"]

    student2 = Student("Ренат", "Луцук", "мужчина")
    student2.finished_courses = ["altium", "git"]
    student2.courses_in_progress = ["c", "python"]

    student3 = Student("Ирина", "Иванова", "женщина")
    student3.finished_courses = ["altium", "git"]
    student3.courses_in_progress = ["c#", "python"]

    reviewer1 = Reviewer("Вася", "Пупкин")
    reviewer1.courses_attached = ["c++", "django", "python"]

    print("\n*****Первый ревьювер выставляет оценки первому студенту*****\n")
    reviewer1.rate_hw(student1, "python", [3, 5, 8, 1])
    reviewer1.rate_hw(student1, "qt", [3, 5, 8, 1])
    reviewer1.rate_hw(student1, "python", [3, 10, 2])
    reviewer1.rate_hw(student1, "c++", [3, 10, 2])

    print("\n*****Первый ревьювер выставляет оценки второму студенту*****\n")
    reviewer1.rate_hw(student2, "django", [3, 5, 8, 1])
    reviewer1.rate_hw(student2, "altium", [3, 5, 8, 1])
    reviewer1.rate_hw(student2, "python", [3, 2])
    reviewer1.rate_hw(student2, "c", [3, 2])

    print("\n*****Первый ревьювер выставляет оценки третьему студенту*****\n")
    reviewer1.rate_hw(student3, "django", [3, 5, 8, 1])
    reviewer1.rate_hw(student3, "altium", [3, 5, 8, 1])
    reviewer1.rate_hw(student3, "python", [3, 2, 8, 7])
    reviewer1.rate_hw(student3, "c#", [3, 2])

    reviewer2 = Reviewer("Глеб", "Федоров")
    reviewer2.courses_attached = ["c", "c#", "python"]

    print("\n*****Второй ревьювер выставляет оценки первому студенту*****\n")
    reviewer2.rate_hw(student1, "python", [3, 5, 8, 1])
    reviewer2.rate_hw(student1, "qt", [3, 5, 8, 1])
    reviewer2.rate_hw(student1, "python", [3, 10, 2])
    reviewer2.rate_hw(student1, "c++", [3, 10, 2])

    print("\n*****Второй ревьювер выставляет оценки второму студенту*****\n")
    reviewer2.rate_hw(student2, "django", [3, 5, 8, 1])
    reviewer2.rate_hw(student2, "altium", [3, 5, 8, 1])
    reviewer2.rate_hw(student2, "python", [3, 2])
    reviewer2.rate_hw(student2, "c", [3, 2])

    print("\n*****Второй ревьювер выставляет оценки третьему студенту*****\n")
    reviewer2.rate_hw(student3, "django", [3, 5, 8, 1])
    reviewer2.rate_hw(student3, "altium", [3, 5, 8, 1])
    reviewer2.rate_hw(student3, "python", [3, 2, 8, 7])
    reviewer2.rate_hw(student3, "c#", [3, 2])

    lecturer1 = Lecturer("Стив", "Джобс")
    lecturer1.courses_attached = ["git", "c++", "python"]

    print("\n*****Первый студент выставляет оценки первому лектору*****\n")
    student1.rate_lecturer("git", lecturer1, [6, 5, 3, 2])
    student1.rate_lecturer("c#", lecturer1, [6, 5, 3, 2])
    student1.rate_lecturer("python", lecturer1, [4])
    student1.rate_lecturer("c++", lecturer1, [9, 7, 4, 7, 5])

    print("\n*****Второй студент выставляет оценки первому лектору*****\n")
    student2.rate_lecturer("c", lecturer1, [6, 5, 3, 2])
    student2.rate_lecturer("c#", lecturer1, [6, 5, 3, 2])
    student2.rate_lecturer("python", lecturer1, [4, 8, 3])
    student2.rate_lecturer("sql", lecturer1, [9, 7, 4, 7, 5])

    print("\n*****Третий студент выставляет оценки первому лектору*****\n")
    student3.rate_lecturer("kotlin", lecturer1, [6, 5, 3, 2])
    student3.rate_lecturer("c#", lecturer1, [6, 5, 3, 2])
    student3.rate_lecturer("python", lecturer1, [1, 4, 9, 10])
    student3.rate_lecturer("django", lecturer1, [9, 7, 4, 7, 5])

    lecturer2 = Lecturer("Джефф", "Безос")
    lecturer2.courses_attached = ["с#", "c++", "c"]

    print("\n*****Первый студент выставляет оценки второму лектору*****\n")
    student1.rate_lecturer("git", lecturer2, [6, 5, 3, 2])
    student1.rate_lecturer("c#", lecturer2, [6, 5, 3, 2])
    student1.rate_lecturer("python", lecturer2, [4])
    student1.rate_lecturer("c++", lecturer2, [9, 7, 4, 7, 5])

    print("\n*****Второй студент выставляет оценки второму лектору*****\n")
    student2.rate_lecturer("c", lecturer2, [6, 5, 3, 2])
    student2.rate_lecturer("c#", lecturer2, [6, 5, 3, 2])
    student2.rate_lecturer("python", lecturer2, [4, 8, 3])
    student2.rate_lecturer("sql", lecturer2, [9, 7, 4, 7, 5])

    print("\n*****Третий студент выставляет оценки второму лектору*****\n")
    student3.rate_lecturer("kotlin", lecturer2, [6, 5, 3, 2])
    student3.rate_lecturer("c#", lecturer2, [6, 5, 3, 2])
    student3.rate_lecturer("python", lecturer2, [1, 4, 9, 10])
    student3.rate_lecturer("django", lecturer2, [9, 7, 4, 7, 5])

    print("\n*****Вывод информации по студентам*****\n")
    print("Student1:", student1, "\n")
    print("Student2:", student2, "\n")
    print("Student3:", student3)

    print("\n*****Вывод информации по ревьюверам*****\n")
    print("Reviewer1:", reviewer1, "\n")
    print("Reviewer2:", reviewer2)

    print("\n*****Вывод информации по лекторам*****\n")
    print("Lecturer1:", lecturer1, "\n")
    print("Lecturer2:", lecturer2)

    print("\n*****Сравнение студентов*****\n")
    print(student1 < student2)
    print(student2 > student3)
    print(student1 == student3)

    print("\n*****Подсчет средней оценки всех студентов по определенному курсу*****\n")
    print("python: ", average_rating_students([student1, student2, student3], "python"))
    print("c++: ", average_rating_students([student1, student2, student3], "c++"))

    print("\n*****Подсчет средней оценки всех лекторов по определенному курсу*****\n")
    print("python: ", average_rating_lecturers([lecturer1, lecturer2], "python"))
    print("c++: ", average_rating_lecturers([lecturer1, lecturer2], "c++"))


solution()
