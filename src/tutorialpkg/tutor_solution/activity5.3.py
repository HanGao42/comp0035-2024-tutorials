import sqlite3
from pathlib import Path
import pandas as pd

# Create a SQL connection to our SQLite database and a cursor
db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_normalised.db')
con = sqlite3.connect(db_path)
data_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_data.csv')
df_students = pd.read_csv(data_path)
df_students.to_sql('enrollments', con, if_exists='replace', index=False)
cur = con.cursor()
df_students.to_sql('enrollments', con, if_exists='replace', index=False)
# Select all rows and columns from the student table
cur.execute('SELECT * FROM student')
rows = cur.fetchall()  # Fetches more than 1 row

# Select the student_id column 
cur.execute('SELECT student_id FROM student WHERE student_name="Blue Bird"')
row = cur.fetchone()  # Fetches the first result
