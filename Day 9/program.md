1.product stock management:
stock = {
    "Pen": 20,
    "Book": 15,
    "Pencil": 30
}
stock["Pen"] -= 5
stock["Eraser"] = 10
print("Updated Stock:", stock)

output:
Updated Stock: {'Pen': 15, 'Book': 15, 'Pencil': 30, 'Eraser': 10}

2.Exam result analyzer:
student = {
    "Name": "Rani",
    "Marks": {
        "Math": 100,
        "Science": 95,
        "English": 90
    }
}
total = sum(student["Marks"].values())
average = total / len(student["Marks"])
print("Total:", total)
print("Average:", average)

output:
Total:285
Average:95
