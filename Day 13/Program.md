class Student:
   def__init__(self, name, mark1, mark2):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
   def total_marks(self):
        return self.mark1 + self.mark2
   def display(self):
        print("Student Name:", self.name)
        print("Total Marks:", self.total_marks())
   s1 = Student("Sumitha", 95, 90)
   s1.display()

   output:
   Student Name: Sumitha
   Total Marks: 185
