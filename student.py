class Student:
    courseMarks = {}
    name = ''
    def __init__(self, name, family):
        self.name = name
        self.family=family
        
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        sum_grade=0
        count=0
        for i in self.courseMarks.values():
            sum_grade+=i
            count+=1
        return sum_grade/count

        



if __name__ == '__main__':
    student = Student('Bowen', 'Vancouver')
    student.addCourseMark('410', 100)
    student.addCourseMark('400', 90)
    print('Average is: ', student.average())
