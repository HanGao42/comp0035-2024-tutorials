""" sqlite3 pathlib pandas
"""
import sqlite3
from pathlib import Path
import pandas as pd

def create_database(db_path, df):
    # Create a connection to the database using sqlite3.
    conn = sqlite3.connect(db_path)

    # Save the dataframe to the database, this will create a table called 'enrollments' and replace it if
    # it exists. The index column is not saved to the table.
    # If the file does not exist then it will be created.
    df.to_sql('enrollments', conn, if_exists='replace', index=False)

    # Close the connection.
    conn.close()


if __name__ == '__main__':
    db_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'enrollments_normalised.db')
    data_path = Path(__file__).parent.parent.joinpath('data_db_activity', 'student_data.csv')
    df_students = pd.read_csv(data_path)
    create_database(db_path, df_students)


""" unfinish """