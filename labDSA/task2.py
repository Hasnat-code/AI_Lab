roll_numbers = {101, 102, 103, 104, 105}

students = {
    "Ali": 75,
    "Sara": 45,
    "Ahmed": 60,
    "Hina": 30,
    "Usman": 85
}

for name, marks in students.items():
    if marks > 50:
        print(name, marks)