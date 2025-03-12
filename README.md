## INTELLIGENT COURSEWORK EVALUATION AND PREDICTION (ICEP) SYSTEM DOCUMENTATION
## COURSEWORK PERFORMANCE ANALYZER - PREDICTING FINAL UNIVERSITY EXAM ELIGIBILITY

- 📍 **Location**: Dodoma, Tanzania
- 📧 **Email**: [sashashamsia@gmail.com](mailto:sashashamsia@gmail.com)
- 📱 **WhatsApp**: [+255675839840](https://wa.me/255675839840)
- 🌐 **Demo**: [Online](https://opensciences.pythonanywhere.com/)

### The System Will Analyze Student Coursework to Determine Final University Examination Eligibility:

| #  | Analysis Task |
|----|-----------------------------------------------------------------------------------------------------------------------------------------|
| 1  | The system will predict the subject in which most students will fail the university exam based on coursework scores below 20. It will provide the subject name and the number of failing students. |
| 2  | The system will predict the subject in which most students will pass the university exam based on coursework scores of 20 or above. It will provide the subject name and the number of passing students. |
| 3  | The system will predict the subject in which most students will achieve high distinction in the university exam based on coursework scores above 30. It will provide the subject name and the number of high-achieving students. |
| 4  | The system will list the names of students who are at risk of failing the university exam due to coursework scores below 20. It will provide the subject name and the number of failing students. |
| 5  | The system will list the names of students who are eligible to sit for the university exam based on coursework scores of 20 or above. It will provide the subject name and the number of passing students. |
| 6  | The system will list the names of students who are likely to achieve high distinction in the university exam based on coursework scores above 30. It will provide the subject name and the number of high-achieving students. |
| 7  | The system will identify departments where a significant number of students may be ineligible to sit for the university exam due to coursework scores below 20. |
| 8  | The system will identify departments where a significant number of students are eligible to sit for the university exam with coursework scores of 20 or above. |
| 9  | The system will identify departments where a significant number of students are likely to achieve high distinction with coursework scores above 30. |
| 10 | The system will provide an overall analysis of student performance to determine how coursework affects eligibility for the university exam. |
| 11 | The system will display the overall count of students eligible and ineligible to sit for the university exam based on coursework performance. |

## 1. Overview

The Intelligent Coursework Evaluation and Prediction (ICEP) system is designed to analyze student coursework performance and predict their likelihood of success in university exams. This system employs machine learning models to provide valuable insights to educators and students.

## 2. Technologies Used

* **Backend:**
    * Python (Flask framework)
    * MySQL (Database)
    * Pandas (Data manipulation)
    * Scikit-learn (Machine learning)
    * Pymysql (Mysql connection)
* **Frontend:**
    * HTML
    * JavaScript
    * CSS
    * Bootstrap
    * Google Fonts
    * Font Awesome

## 3. System Functionality

The ICEP system offers the following features, as presented in the HTML template:

1.  **System Overview:**
    * The system is titled "Intelligent Coursework Evaluation and Prediction (ICEP)."
    * It is described as a "CourseWork Performance Analyzer - Predicting University Exam Outcomes."
    * The system's confidence in its predictions, based on the machine learning model, is displayed as both a decimal and a percentage. For example: "With a confidence ML Model Performance of `{{ accuracy}}` or `{{ accuracy * 100 | round(2) }}%`."

2.  **Overall Pass/Fail Percentages:**
    * The system displays the overall percentage of students predicted to pass and fail.
    * Progress bars visually represent these percentages.
    * Example: Percentage who passed: `{{ (total_passed / df.shape[0]) * 100 | round(2) }}%`
    * Example: Percentage who failed: `{{ (total_failed / df.shape[0]) * 100 | round(2) }}%`

3.  **Key Performance Indicators (KPIs):**
    * Displays the total number of students predicted to pass and fail using cards with icons.
    * Also shows the overall pass percentage.
    * Total Passed: `{{ total_passed }}`
    * Total Failed: `{{ total_failed }}`
    * Pass Percentage: `{{ (total_passed / df.shape[0]) * 100 | round(2) }}%`

4.  **Courses and Students at Risk of Failure:**
    * Lists courses where students are likely to fail, along with the predicted number of failures per course.
    * Provides a table of students predicted to fail, including their names and courses.
    * Courses Where Students Might Fail Exams.
    * Students Who Might Fail Exams.

5.  **Courses and Students Likely to Pass:**
    * Lists courses where students are likely to pass, along with the predicted number of passes per course.
    * Provides a table of students predicted to pass, including their names and courses.
    * Courses Where Students Might Pass Exams.
    * Students Who Might Pass Exams.

6.  **Departments at Risk of Failure and Likely to Pass:**
    * Lists departments with high failure rates, showing the failure rate for each.
    * Lists departments with high success rates, showing the success rate for each.
    * Departments Where Students Might Fail Exams.
    * Departments Where Students Might Pass Exams.

7.  **Courses and Students with High Coursework Scores:**
    * Lists courses where students achieved high coursework scores (over 30).
    * Provides a table of students with high coursework scores, including their names and courses.
    * Courses With High Classwork Scores (Over 30).
    * Students With High Classwork Scores (Over 30).
    * Departments With High Classwork Scores (Over 30).

8.  **Overall Student Performance Summary:**
    * Provides a summary of overall student performance, including the number of students who passed and failed, and the corresponding percentages.
    * How Students Did Overall (Pass or Fail)

9.  **Overall Student Count Summary:**
    * Provides a summary of the number of students that are predicted to pass or fail.
    * Number of Students (Pass or Fail)

## 4. Backend Technologies

The ICEP system utilizes the following backend technologies to process and analyze student data:

* **Python (Flask Framework):**
    * Flask is a lightweight web framework that enables the development of web applications in Python. It's used to create the API endpoints and manage the application's logic.
* **MySQL (Database):**
    * MySQL is a relational database management system used to store and manage student data, including coursework assessments, student information, and course details.
* **Pandas (Data Manipulation):**
    * Pandas is a powerful Python library used for data manipulation and analysis. It's used to process and transform the data retrieved from the MySQL database.
* **Scikit-learn (Machine Learning):**
    * Scikit-learn is a machine learning library used to build and train the predictive models. This includes using the RandomForestClassifier to predict student performance in university exams.
* **Pymysql:**
    * Pymysql is a python library that enables python to connect to Mysql database.

## 5. Frontend Technologies

The ICEP system utilizes the following frontend technologies to present data to the user:

* **HTML:**
    * Used for structuring the web page content.
* **JavaScript:**
    * Used for client-side interactivity and data manipulation.
* **CSS:**
    * Used for styling the web page elements.
* **Bootstrap:**
    * Used for responsive design and UI components.
* **Google Fonts:**
    * Used for custom typography.
* **Font Awesome:**
    * Used for icons to enhance visual representation.

## 6. Data Presentation

* The system presents data in a clear and organized manner using cards, lists, tables, and progress bars.
* Data is dynamically generated using template variables.
* Data tables have search and pagination disabled for clean viewing.
* Progress bars are used to visually represent percentage data.
* Cards are used to display key statistics.
* Tables are used to display detailed student and course data.
* Lists are used to display courses and departments.
