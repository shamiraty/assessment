import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def generate_random_data(num_students=5000):
    np.random.seed(42)

    departments = ['Science', 'Arts', 'Engineering', 'Business', 'Education']
    programs = {
        'Science': ['Physics', 'Chemistry', 'Biology', 'Mathematics'],
        'Arts': ['History', 'Literature', 'Philosophy', 'Languages'],
        'Engineering': ['Civil', 'Mechanical', 'Electrical', 'Computer'],
        'Business': ['Accounting', 'Marketing', 'Finance', 'Management'],
        'Education': ['Primary', 'Secondary', 'Special Needs', 'Early Childhood']
    }
    courses = {
        'Physics': ['Physics 101', 'Physics 102', 'Physics 201'],
        'Chemistry': ['Chemistry 101', 'Chemistry 102'],
        'Biology': ['Biology 101', 'Biology 201'],
        'Mathematics': ['Calculus 1', 'Linear Algebra'],
        'History': ['World History', 'African History'],
        'Literature': ['English Literature', 'Swahili Literature'],
        'Philosophy': ['Ethics', 'Logic'],
        'Languages': ['English', 'French', 'Swahili'],
        'Civil': ['Civil Engineering 101', 'Civil Engineering 201'],
        'Mechanical': ['Mechanical Engineering 101', 'Mechanical Engineering 201'],
        'Electrical': ['Electrical Engineering 101', 'Electrical Engineering 201'],
        'Computer': ['Programming 101', 'Data Structures'],
        'Accounting': ['Financial Accounting', 'Managerial Accounting'],
        'Marketing': ['Marketing Principles', 'Digital Marketing'],
        'Finance': ['Financial Management', 'Investment Analysis'],
        'Management': ['Organizational Behavior', 'Strategic Management'],
        'Primary': ['Primary Education Methods', 'Child Psychology'],
        'Secondary': ['Secondary Education Methods', 'Subject-Specific Pedagogy'],
        'Special Needs': ['Inclusive Education', 'Assistive Technology'],
        'Early Childhood': ['Early Childhood Development', 'Play-Based Learning']
    }

    data = []
    for student_id in range(1, num_students + 1):
        student_name = f'Student {student_id}'
        department = random.choice(departments)
        program = random.choice(programs[department])
        available_courses = courses[program]
        num_courses = random.randint(1, min(4, len(available_courses))) # kurekebisha hapa

        courses_taken = random.sample(available_courses, num_courses)

        for course in courses_taken:
            quiz = np.random.randint(0, 20)
            assignment = np.random.randint(0, 20)
            test1 = np.random.randint(0, 30)
            test2 = np.random.randint(0, 30)
            total_coursework = min(quiz + assignment + test1 + test2, 40)

            data.append({
                'StudentID': student_id,
                'StudentName': student_name,
                'Department': department,
                'Program': program,
                'Course': course,
                'Quiz': quiz,
                'Assignment': assignment,
                'Test1': test1,
                'Test2': test2,
                'TotalCoursework': total_coursework
            })

    return pd.DataFrame(data)

df = generate_random_data()

features = ['TotalCoursework']
target = 'UE_PredictedResult'
df['UE_PredictedResult'] = df['TotalCoursework'].apply(lambda x: 1 if x >= 20 else 0)

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

df['PredictedUE'] = model.predict(df[features])

failed_courses = df[df['PredictedUE'] == 0]['Course'].unique()
passed_courses = df[df['PredictedUE'] == 1]['Course'].unique()

failed_students = df[df['PredictedUE'] == 0]
passed_students = df[df['PredictedUE'] == 1]

department_results = df.groupby('Department')['PredictedUE'].mean()

total_passed = df['PredictedUE'].sum()
total_failed = len(df) - total_passed

print("\n1. Kozi zenye uwezekano wa kufeli kwenye University Exam:")
print(failed_courses)
print(f"Idadi ya wanafunzi wanaotarajiwa kufeli kwenye University Exam: {total_failed}")

print("\n2. Kozi zenye uwezekano wa kufaulu kwenye University Exam:")
print(passed_courses)
print(f"Idadi ya wanafunzi wanaotarajiwa kufaulu kwenye University Exam: {total_passed}")

print("\n3. Kozi zenye ufaulu wa juu (Coursework > 30):")
print(df[df['TotalCoursework'] > 30]['Course'].unique())
print(f"Idadi ya wanafunzi wenye coursework > 30: {len(df[df['TotalCoursework'] > 30])}")

print("\n4. Wanafunzi wanaotarajiwa kufeli kwenye University Exam:")
print(failed_students[['StudentName', 'Course']])

print("\n5. Wanafunzi wanaotarajiwa kufaulu kwenye University Exam:")
print(passed_students[['StudentName', 'Course']])

print("\n6. Wanafunzi wenye ufaulu wa juu (Coursework > 30):")
print(df[df['TotalCoursework'] > 30][['StudentName', 'Course']])

print("\n7. Idara zenye uwezekano wa kufelisha kwenye University Exam:")
print(department_results[department_results < 0.5])

print("\n8. Idara zenye uwezekano wa kufaulisha kwenye University Exam:")
print(department_results[department_results >= 0.5])

print("\n9. Idara zenye ufaulu wa juu (Coursework > 30):")
print(df[df['TotalCoursework'] > 30]['Department'].unique())

print("\n10. Muhtasari wa Jumla (Ufaulu/Ufaulu Duni):")
print(f"Jumla ya wanafunzi waliofaulu Courseworks: {total_passed}")
print(f"Jumla ya wanafunzi waliofeli Courseworks: {total_failed}")
print(f"Asilimia ya ufaulu Courseworks: {(total_passed / len(df)) * 100:.2f}%")
print(f"Asilimia ya ufaulu duni Courseworks: {(total_failed / len(df)) * 100:.2f}%")

print("\n11. Muhtasari wa Jumla (Idadi ya Wanafunzi):")
print(f"Idadi ya wanafunzi waliofaulu: {total_passed}")
print(f"Idadi ya wanafunzi waliofeli: {total_failed}")