import os
os.chdir(r'C:\Users\levin\Desktop')
stulist = open('students_list.txt','w')


class Students:
    stu = 0

    def __init__(self, name, lname, subject, grade):
        self.name = name
        self.lname = lname
        self.subject = subject
        self.grade = grade
        Students.stu += 1

    def display(self):
        print("total amount of students is %d" % Students.stu)

    def display1(self):
        print('name:' + self.name + '  Last name:' + self.lname + '  Subject:' + self.subject + '  Grade:' + self.grade)


print('welcome to the students list program')
print('how to use?\nq -- Close the program\nAdd -- Add students\nDisplay -- display student '
               'information\nTotal -- amount of students\n')
while True:
    choose = input("choose an option you desire ")
    if choose == 'q':
        break
    if choose == 'Add':
        first_name = input('Enter students name: ')
        last_name = input('Enter students last name: ')
        subject = input('Enter the subject of  exam: ')
        grade = input('Enter students grade: ')
        student = Students(first_name, last_name, subject, grade)
        f = str('name:' + student.name + '  Last name:' + student.lname + '  Subject:' + student.subject + '  Grade:' + student.grade)
        stulist.write(f)
        print('The details collected and will be listed in the list')
        stulist.close()
        continue
    if choose == 'Display':
        student.display1()
        continue
    if choose == 'Total':
        print("total amount of students is %d" % Students.stu)
        continue
    else:
        print('you need to choose one of th options only')



