from flask import Flask, render_template
import pymysql
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Database connection
conn = pymysql.connect(host='localhost', user='root', password='', database='assessment')
cursor = conn.cursor()

# Create tables if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    StudentID INT PRIMARY KEY AUTO_INCREMENT,
                    StudentName VARCHAR(255),
                    Department VARCHAR(255),
                    Program VARCHAR(255)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                    CourseID INT PRIMARY KEY AUTO_INCREMENT,
                    StudentID INT,
                    Course VARCHAR(255),
                    Quiz INT,
                    Assignment INT,
                    Test1 INT,
                    Test2 INT,
                    TotalCoursework INT,
                    FOREIGN KEY (StudentID) REFERENCES students(StudentID)
                )''')

conn.commit()

# Generate and insert data
def generate_and_insert_data(num_students=5000):
    np.random.seed(42)
    
    departments = ['Science and IT', 'Humanities', 'Engineering', 'Business', 'Education']
    programs = {
        'Science and IT': ['Physics', 'Chemistry', 'Biology', 'Mathematics'],
        'Humanities': ['History', 'Literature', 'Philosophy', 'Languages'],
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
    
    for student_id in range(1, num_students + 1):
        student_name = f'Student {student_id}'
        department = random.choice(departments)
        program = random.choice(programs[department])
        cursor.execute("INSERT INTO students (StudentName, Department, Program) VALUES (%s, %s, %s)",
                       (student_name, department, program))
        conn.commit()
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        student_db_id = cursor.fetchone()[0]
        
        available_courses = courses[program]
        num_courses = random.randint(1, min(4, len(available_courses)))
        courses_taken = random.sample(available_courses, num_courses)
        
        for course in courses_taken:
            quiz = np.random.randint(0, 20)
            assignment = np.random.randint(0, 20)
            test1 = np.random.randint(0, 30)
            test2 = np.random.randint(0, 30)
            total_coursework = min(quiz + assignment + test1 + test2, 40)
            
            cursor.execute("INSERT INTO courses (StudentID, Course, Quiz, Assignment, Test1, Test2, TotalCoursework) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (student_db_id, course, quiz, assignment, test1, test2, total_coursework))
            conn.commit()

generate_and_insert_data()

# Load data from MySQL
df = pd.read_sql("SELECT students.StudentID, StudentName, Department, Program, Course, Quiz, Assignment, Test1, Test2, TotalCoursework FROM students JOIN courses ON students.StudentID = courses.StudentID", conn)

features = ['TotalCoursework']
df['UE_PredictedResult'] = df['TotalCoursework'].apply(lambda x: 1 if x >= 20 else 0)

X = df[features]
y = df['UE_PredictedResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

df['PredictedUE'] = model.predict(df[features])

failed_courses = df[df['PredictedUE'] == 0]['Course'].unique()
passed_courses = df[df['PredictedUE'] == 1]['Course'].unique()

failed_students = df[df['PredictedUE'] == 0]
passed_students = df[df['PredictedUE'] == 1]

department_results = df.groupby('Department')['PredictedUE'].mean()

total_passed = df['PredictedUE'].sum()
total_failed = len(df) - total_passed

@app.route('/')
def index():
    return render_template('index.html',
                           accuracy=accuracy,
                           failed_courses=failed_courses,
                           passed_courses=passed_courses,
                           high_coursework_courses=df[df['TotalCoursework'] > 30]['Course'].unique(),
                           failed_students=failed_students,
                           passed_students=passed_students,
                           high_coursework_students=df[df['TotalCoursework'] > 30],
                           failed_departments=department_results[department_results < 0.5],
                           passed_departments=department_results[department_results >= 0.5],
                           high_coursework_departments=df[df['TotalCoursework'] > 30]['Department'].unique(),
                           total_passed=total_passed,
                           total_failed=total_failed,
                           df=df)

if __name__ == '__main__':
    app.run(debug=True)
