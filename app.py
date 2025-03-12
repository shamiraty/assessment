from flask import Flask, render_template
import pymysql
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Database connection
conn = pymysql.connect(host='localhost', user='root', password='', database='assessment')
cursor = conn.cursor()

# Load data from MySQL
df = pd.read_sql("""
    SELECT students.StudentID, StudentName, Department, Program, Course, 
           Quiz, Assignment, Test1, Test2, TotalCoursework 
    FROM students 
    JOIN courses ON students.StudentID = courses.StudentID
""", conn)

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
