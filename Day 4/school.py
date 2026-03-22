class Student:
    def __init__(self, name,current_class, id):
       self.name= name
       self.id= id
       self.curent_class=current_class

    def __repr__(self):
        return f'student with name:{self.name}, class: {self.curent_class}, id: {self.id} '

alia=Student("alia",9,1)
print(alia.name,alia.id, alia.curent_class)

# but we can print direct alia by __repr__  method
print(alia)

class teacher:
    def __init__(self,name, subject, id):
        self.name= name
        self.subject= subject
        self.id= id

    def __repr__(self):
        return f'Teacher with name:{self.name}, class: {self.subject}, id: {self.id} '
    
Shushra= teacher("Shushra","dbms",101)
print(Shushra)

class School:
    def __init__(self,name):
        self.name=name
        self.teachers= []
        self.stu= []

    def add_teacher(self, name, subject ):
        id= len(self.teachers)+100
        sir =teacher(name,subject, id)
        self.teachers.append(sir)

    def enroll_studnt(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id= len(self.stu)+1
            student= Student(name, 'c')
            self.stu.append(student)
            return f'{name} is enroll with id:- {id}, extra money {fee-6500}'
    def __repr__(self):
        print('welcome to', self.name)
        print('---------OUR TEACHERS')
        for t in self.teachers:
            print(t)

        print('----------OUR STUDNTS--------')
        for s in self.stu:
            print(s)
        
phitro = School('Phitron')
phitro.enroll_studnt('alia',5200)
phitro.enroll_studnt('rani',8000)
phitro.enroll_studnt('musa',7000)
phitro.enroll_studnt('kuddus',10000)

phitro.add_teacher('Tom',"ds")

print(phitro)