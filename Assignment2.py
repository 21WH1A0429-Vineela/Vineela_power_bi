university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}


# 1.print all the students name and majors 

# print([university_data[i]['name'] for i in university_data])

# for stdid, stdinfo in university_data.items():
#     print(f"Student_name: {stdinfo['name']}")
#     print(f"Student_major: {stdinfo['major']}")
#     print()

# 2.average score per course  per student 

# for stdid, stdinfo in university_data.items():
#     print(f"Student: {stdinfo['name']}")
#     for courses, scores in stdinfo['courses'].items():  
#         avg = sum(scores.values())/ len(scores)
#         print(f'Course: {courses}, Average_score: {avg}')
#     print()


# 3. find who scored >90 in final of python101 

# for stdid, stdinfo in university_data.items():
#     print(f"Student_name: {stdinfo['name']}")
#     for courses, scores in stdinfo['courses'].items():
#         if courses == "Python101" and scores['final'] > 90:
#             print(f"Scored: {scores['final']}")
#             print()

# 4.Add new course for AI101 for student S101

# university_data["S101"]["courses"]["AI101"] = {"midterm": 0, "final": 0, "project": 0}


# 5.Print average for each course 

for stdinfo in university_data.items():
    for courses, scores in stdinfo['courses'].items():  
        avg = sum(scores.values())/ len(scores)
        print(f'Course: {courses}, Average_score: {avg}')
    print()