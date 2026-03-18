import random
import json
from typing import Dict, List

# ============================================================
# Synthetic school scheduling data generator
# ------------------------------------------------------------
# This program ONLY generates data.
# It does NOT build or solve a schedule.
#
# Data generated:
# - students
# - courses
# - sections
# - teachers
# - time slots
# - classroom capacities
# - student top-5 preferences
# ============================================================

random.seed(42)

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
NUM_STUDENTS = 200
NUM_TEACHERS = 24
NUM_COURSES = 30

MIN_SECTIONS_PER_COURSE = 1
MAX_SECTIONS_PER_COURSE = 4

MIN_CAPACITY = 18
MAX_CAPACITY = 30

# A small weekly timetable model
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
PERIODS = [1, 2, 3, 4, 5, 6]

# Example course name bank
COURSE_NAME_BANK = [
    "Mathematics",
    "English Literature",
    "Biology",
    "Chemistry",
    "Physics",
    "History",
    "Geography",
    "Economics",
    "Psychology",
    "Computer Science",
    "Art",
    "Music",
    "Drama",
    "Physical Education",
    "Business Studies",
    "Environmental Systems",
    "Philosophy",
    "Global Politics",
    "Design Technology",
    "Statistics",
    "French",
    "Spanish",
    "German",
    "Mandarin",
    "Media Studies",
    "Robotics",
    "Web Development",
    "Data Science",
    "Sociology",
    "Creative Writing",
]

FIRST_NAMES = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", "Quinn",
    "Cameron", "Blake", "Parker", "Skyler", "Rowan", "Hayden", "Drew", "Reese",
    "Elliot", "Charlie", "Emerson", "Finley", "Harper", "Jamie", "Logan", "Micah",
    "Noah", "Olivia", "Liam", "Emma", "Sophia", "Mason", "Isabella", "Lucas",
    "Mia", "Amelia", "Ethan", "Abigail", "James", "Ella", "Benjamin", "Scarlett"
]

LAST_NAMES = [
    "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson",
    "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
    "Clark", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King",
    "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Carter", "Mitchell"
]

ROOM_PREFIXES = ["A", "B", "C", "D", "E", "Lab", "Sci", "Art", "Gym", "Tech"]


# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def generate_unique_full_names(count: int) -> List[str]:
    names = set()
    while len(names) < count:
        full_name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        names.add(full_name)
    return sorted(names)


def generate_time_slots(days: List[str], periods: List[int]) -> List[str]:
    return [f"{day}-P{period}" for day in days for period in periods]


def make_room_name() -> str:
    prefix = random.choice(ROOM_PREFIXES)
    number = random.randint(101, 499)
    return f"{prefix}{number}"


def choose_top_five_courses(courses: List[Dict]) -> List[str]:
    # random.sample guarantees uniqueness
    return random.sample([course["course_id"] for course in courses], 5)


# ------------------------------------------------------------
# Data generation
# ------------------------------------------------------------
def generate_courses() -> List[Dict]:
    courses = []
    for i in range(NUM_COURSES):
        course_id = f"C{i+1:03d}"
        course_name = COURSE_NAME_BANK[i % len(COURSE_NAME_BANK)]
        courses.append({
            "course_id": course_id,
            "course_name": course_name
        })
    return courses


def generate_teachers(num_teachers: int) -> List[Dict]:
    teacher_names = generate_unique_full_names(num_teachers)
    teachers = []
    for i, name in enumerate(teacher_names, start=1):
        teacher_id = f"T{i:03d}"
        teachers.append({
            "teacher_id": teacher_id,
            "teacher_name": name
        })
    return teachers


def generate_students(num_students: int, courses: List[Dict]) -> List[Dict]:
    student_names = generate_unique_full_names(num_students)
    students = []
    for i, name in enumerate(student_names, start=1):
        student_id = f"S{i:04d}"
        students.append({
            "student_id": student_id,
            "student_name": name,
            "top_5_preferences": choose_top_five_courses(courses)
        })
    return students


def generate_sections(
    courses: List[Dict],
    teachers: List[Dict],
    time_slots: List[str]
) -> List[Dict]:
    sections = []
    used_teacher_time_pairs = set()

    for course in courses:
        num_sections = random.randint(MIN_SECTIONS_PER_COURSE, MAX_SECTIONS_PER_COURSE)

        for section_number in range(1, num_sections + 1):
            section_id = f"{course['course_id']}-SEC{section_number}"

            # Teacher assignment:
            # keep trying until we find a teacher + time slot combination
            # that is not already used by that teacher
            attempts = 0
            while True:
                teacher = random.choice(teachers)
                time_slot = random.choice(time_slots)
                teacher_time_pair = (teacher["teacher_id"], time_slot)

                if teacher_time_pair not in used_teacher_time_pairs:
                    used_teacher_time_pairs.add(teacher_time_pair)
                    break

                attempts += 1
                if attempts > 500:
                    # Fallback: force a different slot if the dataset becomes tight
                    available_pairs = [
                        (t["teacher_id"], ts)
                        for t in teachers
                        for ts in time_slots
                        if (t["teacher_id"], ts) not in used_teacher_time_pairs
                    ]
                    if not available_pairs:
                        raise RuntimeError("No teacher/time-slot pairs remain.")
                    teacher_id, time_slot = random.choice(available_pairs)
                    used_teacher_time_pairs.add((teacher_id, time_slot))
                    teacher = next(t for t in teachers if t["teacher_id"] == teacher_id)
                    break

            room = make_room_name()
            capacity = random.randint(MIN_CAPACITY, MAX_CAPACITY)

            sections.append({
                "section_id": section_id,
                "course_id": course["course_id"],
                "course_name": course["course_name"],
                "teacher_id": teacher["teacher_id"],
                "teacher_name": teacher["teacher_name"],
                "time_slot": time_slot,
                "room": room,
                "capacity": capacity
            })

    return sections


def build_dataset() -> Dict:
    time_slots = generate_time_slots(DAYS, PERIODS)
    courses = generate_courses()
    teachers = generate_teachers(NUM_TEACHERS)
    students = generate_students(NUM_STUDENTS, courses)
    sections = generate_sections(courses, teachers, time_slots)

    dataset = {
        "metadata": {
            "random_seed": 42,
            "num_students": len(students),
            "num_teachers": len(teachers),
            "num_courses": len(courses),
            "num_sections": len(sections),
            "num_time_slots": len(time_slots)
        },
        "time_slots": time_slots,
        "courses": courses,
        "teachers": teachers,
        "sections": sections,
        "students": students
    }

    return dataset


# ------------------------------------------------------------
# Optional export helpers
# ------------------------------------------------------------
def save_json(data: Dict, filename: str = "synthetic_school_data.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":
    dataset = build_dataset()

    # Print a short preview
    print("Synthetic school scheduling data generated.")
    print()
    print("Metadata:")
    for key, value in dataset["metadata"].items():
        print(f"  {key}: {value}")

    print("\nSample course:")
    print(dataset["courses"][0])

    print("\nSample teacher:")
    print(dataset["teachers"][0])

    print("\nSample section:")
    print(dataset["sections"][0])

    print("\nSample student:")
    print(dataset["students"][0])

    # Save full dataset to JSON
    save_json(dataset)
    print("\nFull dataset saved to synthetic_school_data.json")
