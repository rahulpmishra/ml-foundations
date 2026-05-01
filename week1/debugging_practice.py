def calculate_average(numbers):
    if len(numbers) == 0: return 0
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)
    return average

def process_student_scores(students):
    results = {}
    for student in students:
        name = student['name']
        scores = student['scores']
        avg = calculate_average(scores)
        results[name] = avg
    return results

students_data = [
    {'name': 'Alice', 'scores': [85, 92, 78, 95]},
    {'name': 'Bob', 'scores': [70, 68, 72, 75]},
    {'name': 'Charlie', 'scores': []},   
    {'name': 'Diana', 'scores': [90, 88, 92]},
]

results = process_student_scores(students_data)
print(results)