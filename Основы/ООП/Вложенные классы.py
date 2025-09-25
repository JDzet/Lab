"""
class Women:
    title = 'object class for fild title'
    photo = 'object class for fild photo'
    ordering = "object class for fild ordering"


    def __init__(self, user, pws):
        self._user = user
        self._psw = pws
        self.meta = self.Meta(user + '@' + pws)

    class Meta:
        ordering = ['id']
        def __init__(self, access):
            self._access = access


w = Women("root", "12345")



print(w.ordering)
print(w.Meta.ordering) # Обращаемся к атребутам вложенного класса
print(w.__dict__)
print(w.meta.__dict__)
"""


class University:
    def __init__(self, UnivName):
        self.UnivName = UnivName
        self.Students = []

    def AddStudent(self, name, faculty, score):
        s = self.Student(name, faculty, score)
        self.Students.append(s)
        print(f"Студент - {s.name} зарегистрирован")

    def _SearchFaculty(self, faculty):
        return [x for x in self.Students if x.faculty.lower() == faculty.lower()]


    def ShowFacultGPA(self, faculty):
        StudentsFaculty = self._SearchFaculty(faculty)
        if not StudentsFaculty:
            print("Данных о таком фокультете нет")
            return
        GPA = 0
        for g in StudentsFaculty:
            GPA += g.score
        print(GPA / len(StudentsFaculty))



    class Student:
        def __init__(self, name, faculty, score):
            self.name = name
            self.faculty = faculty
            self.score = score


u = University("USA")
u.AddStudent("A","1",4)
u.AddStudent("C","1",3)
u.AddStudent("D","2",5)
u.AddStudent("B","2",3)
u.AddStudent("Q","1",5)


u.ShowFacultGPA("2")