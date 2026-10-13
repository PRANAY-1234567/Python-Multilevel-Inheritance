'''class Grandpa:
    "Statement"

class Father(Grandpa):
    "Statement"

class child(Father):
    "Statement"'''

'''class Grandpa:
    def villa(self):
        print("💕")

class Father(Grandpa):
    def villa(self):
        super().villa()
        print("Villa")

class Child(Father):
    def villa(self):
        print("😑")

c=Child()
c.villa'''

'''class Grandpa:
    def __init__(self):
        print("💕")

class Father(Grandpa):
    def __innit__(self):
        super().__init__()
        print("Villa")

class Child(Father):
    def __init__(self):
        super().__init__()
        print("😑")

c=Child()
c.villa'''
#-------------------===========================----------------------====================================
"""class PySpider:
    def __init__(self, Total_s, total_Girl, Total_Boy):
        self.t = Total_s
        self.tg = total_Girl
        self.tb = Total_Boy

    def Information(self):
        print(f'Total Students in PY {self.t}\n'
              f'Total Girl {self.tg}\n'
              f'Total Boy {self.tb}')

class Subject(PySpider):
    def __init__(self, Total_s, total_Girl, Total_Boy, Subject, total_Class):
        super().__init__(Total_s, total_Girl, Total_Boy)
        self.name = Subject
        self.tc = total_Class


    def Data(self):
         print(f'Subject Name Is {self.name}\n'
            f'Total Class Output {self.tc}')


class Result(Subject):
    def __init__(self, Total_s, total_Girl, Total_Boy, Subject, total_Class, total_marks, Grade):
        super().__init__(Total_s, total_Girl, Total_Boy, Subject, total_Class)
        self.total_marks = total_marks
        self.g = Grade

    def final(self):
        print(f'Total Marks is {self.total_marks}\n'
              f'Total Grade {self.g}')

r=Result(250, 50, 30, "Python", 900, 20, "A++")
r.Information()
r.Data()
r.final()"""