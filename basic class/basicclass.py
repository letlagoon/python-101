class School:
    # attribute
    SchoolName = 'ลุงวิศวกร สอนคำนวน'

    # Constuctor 
    def __init__(self, subject='Python Programming'):
        print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        self.subject = subject

    # method
    def hello(self):
        print('สวัสดีตอนเช้า ยินดีต้อนรับนักเรียนทุกคน')

    def teach(self):
        print(f'โรงเรียนนี้ เปิดสอนวิชา {self.subject}')

class Student(School):
    def __init__(self, fullname, level, scores, subject):
        super().__init__(subject)
        self.fullname = fullname
        self.level = level
        self.scores = scores

    def checkGrade(self):
        if self.scores >= 80:
            print(f'วิชา {self.subject} ได้เกรด A')

        elif self.scores >= 70:
            print(f'วิชา {self.subject} ได้เกรด B')

        elif self.scores >= 60:
            print(f'วิชา {self.subject} ได้เกรด C')

        elif self.scores >= 50:
            print(f'วิชา {self.subject} ได้เกรด D')

        else :
            print(f'วิชา {self.subject} ได้เกรด F')
        

# Instance กำหนดชื่อ Opject ของ class 
# school01 = School()
# print(f'ชื่อโรงเรียน : {school01.SchoolName}')        
# school01.hello()
# school01.teach()
print('====================================')
Student01 = Student('สมชาย สายลม', 1, 75, 'Math')
Student01.hello()
print(f'ชื่อโรงเรียน {Student01.SchoolName}')
print(f'ชื่อนักเรียน {Student01.fullname}')
print(f'ระดับชั้น {Student01.level}')
print(f'คะแนนสอบ {Student01.scores}')
Student01.checkGrade()
print('====================================')
Student02 = Student('สมหญิง สายลม', 7, 90, 'English')
Student02.hello()
print(f'ชื่อโรงเรียน {Student02.SchoolName}')
print(f'ชื่อนักเรียน {Student02.fullname}')
print(f'ระดับชั้น {Student02.level}')
print(f'คะแนนสอบ {Student02.scores}')
Student02.checkGrade()
print('====================================')
Student03 = Student('สมปอง สายลม', 12, 49, 'Python Programming')
Student03.hello()
print(f'ชื่อโรงเรียน {Student03.SchoolName}')
print(f'ชื่อนักเรียน {Student03.fullname}')
print(f'ระดับชั้น {Student03.level}')
print(f'คะแนนสอบ {Student03.scores}')
Student03.checkGrade()
