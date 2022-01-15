stu=['Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph', 'Kincaid','Larry']
plants={'V': 'Violets', 'R': 'Radishes', 'G': 'Grass', 'C': 'Clover'}

class Garden:

    def __init__(self, diagram, students=stu):

        self.diagram=[list(x) for x in diagram.split("\n")]
        self.row1=self.diagram[0]
        self.row2=self.diagram[1]
        self.students=sorted(students)

    def plants(self,name):
        sindex=self.students.index(name)*2
        student_plants=[i for i in self.row1[sindex:sindex+2]]+[i for i in self.row2[sindex:sindex+2]]
        return [plants[x] for x in student_plants]
