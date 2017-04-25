#  Dalvir Thind 69341014 and Pok On Cheng 74157306.  ICS 31 Lab sec 5.  Lab asst 8.


from collections import namedtuple

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)

Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])

StudentBody = [sW, sX, sY, sZ]

print()
print('----------------Part C----------------')
print()
print("C.1")
print()
def Students_at_level(Ls:list, string: str) -> list:
    '''Returns a list of students whose class level match the parameter
    '''
    result = []
    for i in Ls:
        if i.level == string:
            result.append(i)
    return result
#print(Students_at_level(StudentBody, "FR"))
for i in Students_at_level(StudentBody, "FR"):
    print(i)
    print()

#C.2
print("C.2")
def Students_in_majors(Ls:list, string: list) -> list:
    '''returns a list of Students that have majors on the specified list
    '''
    result = []
    for i in Ls:
        for n in string:
            if i.major == n:
                result.append(i)
    return result
for i in Students_in_majors(StudentBody, ["PSB", "CS"]):
    print(i)
    print()
print("C.3")

def Students_in_class(Ls:list, string1: str, string2: str) -> list:
    '''returns a list of those Students who are enrolled in the specified class
    '''
    result = []
    for i in Ls:
        if Student_is_enrolled(i, string1, string2):
            result.append(i)
    return result

def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    return (c1.dept and c1.num) == (c2.dept and c2.num)

def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    for i in SL:
        return (c.dept and c.num) == (i.dept and i.num)

def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    for i in S.studylist:
        return (department and coursenum) == (i.dept and i.num)

#print(Students_in_class(StudentBody, "ICS", "31"))
for i in Students_in_class(StudentBody, "ICS", "31"):
    print(i)
    print()

print("C.4")

def Student_names(Ls: list) -> list:
    ''' returns a list of just the names of those students
    '''
    result = []
    for i in Ls:
        result.append(i.name)
    return result
for i in Student_names(StudentBody):
    print(i)
    print()

print("C.5")

#ICS = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']

def Student_major(Ls:list) -> list:
    result = []
    for i in Ls:
        for j in i.studylist:
            for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
                if k == j.dept:
                    result.append(i)
    return result
for i in Student_major(StudentBody):
    print(i)
    print()

def Student_major_name(Ls:list) -> list:
    result = []
    for i in Ls:
        for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
            if k == i.major:
                result.append(i.name)
    return result
for i in Student_major_name(StudentBody):
    print(i)
    print()

def Student_major_senior(Ls:list) -> list:
    result = []
    for i in Ls:
        for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
            if k == i.major:
                if i.level == 'SR':
                    result.append(i.name)
    return result
for i in Student_major_senior(StudentBody):
    print(i)
    print()

def Student_major_number_senior(Ls:list) -> int:
    number = 0
    for i in Ls:
        for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
            if k == i.major:
                if i.level == 'SR':
                    number += 1
    return number
print(Student_major_number_senior(StudentBody))

def Student_major_percentage_senior(Ls:list) -> float:
    total = 0
    number = Student_major_number_senior(Ls)
    for i in Ls:
        for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
            if k == i.major:
                total += 1
    if total != 0:
        return (number / total) * 100
print(Student_major_percentage_senior(StudentBody))


def Student_major_number_freshmen(Ls:list) -> int:
    number = 0
    for i in Ls:
        for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
            if k == i.major:
                if i.level == 'FR':
                    if Student_is_enrolled(i, "ICS", "31"):
                        number += 1
    return number
print(Student_major_number_freshmen(StudentBody))

def Student_major_averageunit_freshmen(Ls:list):
    number = Student_major_number_freshmen(Ls)
    total = 0
    for i in Ls:
        for k in ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']:
            if k == i.major:
                if i.level == 'FR':
                    if Student_is_enrolled(i, "ICS", "31"):
                        for j in i.studylist:
                            total += j.units
    if number != 0:
        return total / number
    else:
        return "There is no freshman in ICS 31"
print(Student_major_averageunit_freshmen(StudentBody))
