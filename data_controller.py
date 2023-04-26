import pandas as pd
import csv
# import mysql.connector
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# Connect to the MySQL database
# def connect_to_db(_host, _user, _password, _database):
#     global cursor, db, db
#     db = mysql.connector.connect(
#         host=_host,
#         user=_user,
#         password=_password,
#         database=_database
#         # host="localhost",
#         # user="yourusername",
#         # password="yourpassword",
#         # database="yourdatabase"
#     )
#     cursor = db.cursor()


# Close the database connection
# def close_db_connection():
#     db.close()


# Create a cursor object to execute SQL queries
def export_metrics():
    global cursor, db
    # Load the CSV data into a pandas DataFrame
    df = pd.read_csv("metrics.csv")

    # Iterate over the rows of the DataFrame and insert them into the database
    for index, row in df.iterrows():
        sql = "INSERT INTO table_name (id, time_stamp, result, reaction_time) VALUES (%s, %s, %s)"
        val = (row['timestamp'], row['result'], row['reaction_time'])
        cursor.execute(sql, val)
        db.commit()

# Patient
# PatientID, FirstName, LastName, D.O.B

# CreateTreatment
def add_patient(first_name, last_name, birth_date):
    global cursor, db
    if cursor:
        try:
            cursor.execute("INSERT INTO patient (first_name, last_name, birth_date) VALUES (?, ?, ?)", (first_name, last_name, birth_date))
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        with open("patients.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, birth_date])


# ReadAllTreatmentsForPatient
def get_patients(filter = None, col_filter = None):
    global cursor, db
    if cursor:
        try:
            if not filter:
                cursor.execute("SELECT * FROM patient")
            else:
                d = {"ID": "id", "First Name": "first_name", "Last Name": "last_name", "Date of Birth": "birth_date"}
                cursor.execute(f"SELECT * FROM patient WHERE {d[col_filter]} LIKE ?", (filter+'%', ))
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
    else:
        patients = list()
        with open("patients.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                patients.append(row)
        return patients


# Get Patient by ID
def get_patient_by_id(patient_id):
    global cursor, db
    if cursor:
        try:
            cursor.execute("SELECT * FROM patient WHERE id=?", (patient_id,))
            return cursor.fetchone()
        except Exception as e:
            print(str(e))
    else:
        with open("patients.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[0]) == patient_id:
                    return row


# UpdateTreatment
def update_patient(patient_id, first_name, last_name, birth_date):
    global cursor, db
    if cursor:
        try:
            cursor.execute("UPDATE patient SET first_name=?, last_name=?, birth_date=? WHERE id=?", (
                first_name,
                last_name,
                birth_date,
                patient_id
            ))
            conn.commit()
        except Exception as e:
            print(str(e))


# DeleteTreatment
def remove_patient(patient_id):
    global cursor, db
    if cursor:
        try:
            cursor.execute("DELETE FROM patient WHERE id = ?", (patient_id, ))
            conn.commit()
            return True
        except Exception as e:
            print(str(e))
            return False



# Treatment
# TreatmentID, PatientID, StartDate, EndDate, Summary

# CreateTreatment
def add_treatment(treatment_name, patient_id, start_date, end_date, summary=""):
    global cursor, db
    if cursor:
        try:
            cursor.execute("INSERT INTO treatment(treatment_name, patient_id, start_date, end_date, summary) VALUES (?, ?, ?, ?, ?)",
                (treatment_name, patient_id, start_date, end_date, summary))
            conn.commit()
        except Exception as e:
            print(str(e))


# ReadAllTreatmentsForPatient
def get_treatments(patient_id, filter = None, col_filter = None):
    global cursor, db
    if cursor:
        try:
            if not filter:
                cursor.execute("SELECT * FROM treatment WHERE patient_id=?", (patient_id,))
            else:
                d = {
                    "Treatment ID": "treatment_id", 
                    "Treatment Name": "treatment_name", 
                    "Start Date": "start_date", 
                    "End Date": "end_date",
                    "Summary": "summary"}
                cursor.execute(f"SELECT * FROM treatment WHERE {d[col_filter]} LIKE ? AND patient_id=?", (filter+'%', patient_id))
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
    else:
        treatments = list()
        with open("treatments.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[2]) == patient_id:
                    treatments.append(row)
        return treatments


# Get Treatment by ID
def get_treatment_by_id(treatment_id):
    global cursor, db
    if cursor:
        try:
            cursor.execute("SELECT * FROM treatment WHERE treatment_id=?", (treatment_id,))
            return cursor.fetchone()
        except Exception as e:
            print(str(e))
    else:
        with open("treatments.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[0]) == int(treatment_id):
                    return row


def get_visit_by_id(visit_id):
    global cursor, db
    if cursor:
        try:
            cursor.execute("SELECT * FROM visit WHERE id=?", (visit_id,))
            return cursor.fetchone()
        except Exception as e:
            print(str(e))


# UpdateTreatment
def update_treatment(treatment_id, treatment_name, start_date, end_date, summary):
    global cursor, db
    if cursor:
        try:
            cursor.execute("UPDATE treatment SET treatment_name=?, start_date=?, end_date=?, summary=? WHERE treatment_id=?",
            (treatment_name, start_date, end_date, summary, treatment_id))
            conn.commit()
        except Exception as e:
            print(str(e))


# DeleteTreatment
def remove_treatment(treatment_id):
    global cursor, db
    if cursor:
        try:
            cursor.execute("DELETE FROM treatment WHERE treatment_id = ?", (treatment_id,))
            conn.commit()
            return True
        except Exception as e:
            print(str(e))
            return False


# Visit
# VisitID, TreatmentID, Date, Summary, AttentionLevel, ExternalSource


# CreateVisit
def add_visit(treatment_id, date, visit_type, summary, attention_level, external_source, doctor_name):
    global cursor, db
    if cursor:
        cursor.execute("""INSERT INTO visit (treatment_id, date, summary, attention_level, external_source, visit_type, doctor_name) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (treatment_id, date, summary, attention_level, external_source, visit_type, doctor_name))
        conn.commit()


# ReadAllVisits
def get_visits(treatment_id, filter = None, col_filter = None):
    global cursor, db
    if cursor:
        try:
            if not filter:
                cursor.execute("SELECT id, treatment_id, date, visit_type, attention_level FROM visit WHERE treatment_id=?", (treatment_id,))
            else:
                d = {
                    "ID": "id", 
                    "Visit Type": "visit_type", 
                    "Date": "date",
                    "Attention Level": "attention_level"}
                cursor.execute(f"SELECT id, treatment_id, date, visit_type, attention_level FROM visit WHERE {d[col_filter]} LIKE ? AND treatment_id=?", (filter+'%', treatment_id))
            return cursor.fetchall()
        except Exception as e:
            print(str(e))
    else:
        visits = list()
        with open("visits.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[2]) == int(treatment_id):
                    visits.append(row)
        return visits


# UpdateVisit
def update_visit(visit_id, summary, attention_level, external_source, doctor_name):
    global cursor, db
    if cursor:
        try:
            cursor.execute("UPDATE visit SET summary=?, attention_level=?, external_source=?, doctor_name=? WHERE id=?", 
            (summary, attention_level, external_source, doctor_name, visit_id))
            conn.commit()
        except Exception as e:
            print(str(e))
    else:
        with open("treatments.csv", mode='a+', newline='') as file:
            reader = csv.reader(file)
            writer = csv.writer(file)
            for row in reader:
                if row["visit_id"] == visit_id:
                    row["summary"] = summary if summary != "" else row["summary"]
                    row["attention_level"] = attention_level if attention_level != "" else row["start_date"]
                    row["external_source"] = external_source if external_source != "" else row["external_source"]
                    writer.writerow(row)
                    break


# DeleteVisit
def remove_visit(visit_id):
    global cursor, db
    if cursor:
        try:
            cursor.execute("DELETE FROM visit WHERE id =?", (visit_id,))
            conn.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
    else:
        df = pd.read_csv("visits.csv")
        df = df[df.visit_id != visit_id]
        df.to_csv("visits.csv", index=False)
