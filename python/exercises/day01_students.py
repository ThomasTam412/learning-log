students = [
    {"name": "thomas", "score": 100},
    {"name": "alice", "score": 99},
    {"name": "bob", "score": 98},
    {"name": "tom", "score": 97},
    {"name": "timi", "score": 100},
]
def print_students(students: list[dict]) -> None:
    if not students:
        print("暫無學生資料")
        return
    for student in students:
        name = student["name"]
        score = student["score"]
        print(f"Student:{name}, {score}分")

def get_avg(students: list[dict]) -> float | None:
    if not students:
        return None
    scores = [s["score"] for s in students]
    avg = sum(scores) / len(scores)
    return avg

print_students(students)
avg = get_avg(students)
print(f"平均分:{avg:.2f}")

above_avg = [stu for stu in students if stu["score"] > avg]

print_students(above_avg)