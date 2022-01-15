class School():
    def __init__(self):
        self.students_grade = {}
        self.check=[]

    def add_student(self, name, grade):
        if name not in self.students_grade:
            self.students_grade[name] = grade
            self.check.append(True)
        else:
            self.check.append(False) 

    def added(self):
        return self.check

    def roster(self):
        sorted_student=sorted(list(self.students_grade.items()),key=lambda x:(x[1],x[0])) 
        new_list=[]
        for i in range(len(sorted_student)):
                new_list.append(sorted_student[i][0])    

        return new_list

    def grade(self, grade_number):
       result = []
        for key, value in self.students_grade.items():
            if value == grade_number:
                result.append(key)

        

          

        return sorted(result)
