students = [
    {"name": "Ali", "score": 90},
    {"name": "Vali", "score": 70},
    {"name": "Sami", "score": 95},
    {"name": "Hasan", "score": 85}
]

students.sort(key=lambda x: x["score"], reverse=True)

print("Reyting:")

place = 1

for student in students:
    print(place, student["name"], student["score"])
    place += 1
