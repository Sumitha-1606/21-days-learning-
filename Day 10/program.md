1.dose1 = {"P1", "P2", "P3", "P4"}
dose2 = {"P3", "P4", "P5"}
fully_vaccinated = dose1 & dose2
print("Fully vaccinated patients:", fully_vaccinated)

output:
Fully vaccinated patients: {'P3', 'P4'}

2.library_A = {"Maths", "Physics", "Chemistry"}
library_B = {"Biology", "Physics", "English"}
all_books = library_A | library_B
print("All subjects:", all_books)

output:
All subjects: {'Maths', 'Physics', 'Chemistry', 'Biology', 'English'}
