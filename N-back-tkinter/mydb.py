from datetime import datetime
import os
import sqlite3

script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, '..', 'database.db')
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

def add_test(visit_id, timestamp, result, reaction_time, got_help, stack_size, expected, question, received, time_diff, elapsed_time, type):
    global cursor, db
    try:
        cursor.execute("""INSERT INTO tests (visit_id, timestamp, result, reaction_time, got_help, stack_size, expected, question, received, time_diff, elapsed_time, type) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (visit_id, timestamp, result, reaction_time, got_help, stack_size, expected, question, received, time_diff, elapsed_time, type))
        conn.commit()
    except Exception as e:
        print(str(e))
        

def add_visit(treatment_id, date, visit_type, summary, attention_level, external_source, doctor_name, recommendation, rec_date, references, ref_date):
    global cursor, db
    if cursor:
        if rec_date:
            rec_date = datetime.strptime(rec_date, "%m/%d/%y").strftime("%m/%d/%Y")
        if ref_date:
            ref_date = datetime.strptime(ref_date, "%m/%d/%y").strftime("%m/%d/%Y")
        cursor.execute("""INSERT INTO visit (treatment_id, date, summary, attention_level, external_source, visit_type, doctor_name, recommendation, recommendation_date, reference, reference_date) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (treatment_id, date, summary, attention_level, external_source, visit_type, doctor_name, recommendation,
            rec_date, references, ref_date))
        conn.commit()
        return cursor.lastrowid


def get_visits(treatment_id, visit_type) -> int:
    """
    Get the current number of the visit type
    """
    global cursor, db
    if cursor:
        cursor.execute(f"SELECT visit_type FROM visit WHERE treatment_id=?", (treatment_id,))
        l = cursor.fetchall()
        answer = 1
        for element in l:
            if visit_type in element[0]:
                answer += 1
        return answer