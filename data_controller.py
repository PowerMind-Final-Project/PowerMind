import pandas as pd
import csv
# import mysql.connector

cursor = None


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
def add_patient(patient_id, first_name, last_name, birth_date):
    global cursor, db
    if cursor:
        try:
            sql = "INSERT INTO patients (patient_id, first_name, last_name, birth_date) VALUES (%s, %s, %s, %s)"
            val = (patient_id, first_name, last_name, birth_date)
            cursor.execute(sql, val)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        with open("patients.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([patient_id, first_name, last_name, birth_date])


# ReadAllTreatmentsForPatient
def get_patients():
    global cursor, db
    if cursor:
        try:
            sql = "SELECT * FROM patients WHERE patient_id=" + patient_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            return result_dataFrame
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
            sql = "SELECT * FROM patients WHERE patient_id=" + patient_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            return result_dataFrame
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
def update_treatment(treatment_id, start_date="", end_date="", summary=""):
    global cursor, db
    if cursor:
        try:
            sql = "SELECT * FROM treatments WHERE treatment_id =" + treatment_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            start_date = start_date if start_date != "" else result_dataFrame[start_date]
            end_date = end_date if end_date != "" else result_dataFrame[end_date]
            summary = summary if summary != "" else result_dataFrame[summary]
            sql = "UPDATE treatments SET start_date=" + start_date + ", end_date=" + end_date + ", summary=" + summary + \
                  " WHERE treatment_id=" + treatment_id + ";"
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        with open("treatments.csv", mode='a+', newline='') as file:
            reader = csv.reader(file)
            writer = csv.writer(file)
            for row in reader:
                if row["treatment_id"] == treatment_id:
                    row["start_date"] = start_date if start_date != "" else row["start_date"]
                    row["end_date"] = end_date if end_date != "" else row["end_date"]
                    row["summary"] = summary if summary != "" else row["summary"]
                    writer.writerow(row)
                    break


# DeleteTreatment
def remove_treatment(treatment_id):
    global cursor, db
    if cursor:
        try:
            sql = "DELETE * FROM treatments WHERE treatment_id =" + treatment_id + ";"
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        df = pd.read_csv("treatments.csv")
        df = df[df.treatment_id != treatment_id]
        df.to_csv("treatments.csv", index=False)



# Treatment
# TreatmentID, PatientID, StartDate, EndDate, Summary

# CreateTreatment
def add_treatment(treatment_name, patient_id, start_date, end_date, summary=""):
    global cursor, db
    if cursor:
        try:
            sql = "INSERT INTO treatments (treatment_name, patient_id, start_date, end_date, summary) VALUES (%s, %s, %s, %s)"
            val = (treatment_name, patient_id, start_date, end_date, summary)
            cursor.execute(sql, val)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        with open("treatments.csv", mode='a+', newline='') as file:
            data = file.readlines()
            print(data)
            # new_id = data[-1][0] + 1
            new_id = 4
            writer = csv.writer(file)
            writer.writerow([new_id, treatment_name, patient_id, start_date, end_date, summary])


# ReadAllTreatmentsForPatient
def get_treatments(patient_id):
    global cursor, db
    if cursor:
        try:
            sql = "SELECT * FROM treatments WHERE patient_id=" + patient_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            return result_dataFrame
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
            sql = "SELECT * FROM treatments WHERE treatment_id=" + treatment_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            return result_dataFrame
        except Exception as e:
            print(str(e))
    else:
        with open("treatments.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[0]) == int(treatment_id):
                    return row


# UpdateTreatment
def update_treatment(treatment_id, start_date="", end_date="", summary=""):
    global cursor, db
    if cursor:
        try:
            sql = "SELECT * FROM treatments WHERE treatment_id =" + treatment_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            start_date = start_date if start_date != "" else result_dataFrame[start_date]
            end_date = end_date if end_date != "" else result_dataFrame[end_date]
            summary = summary if summary != "" else result_dataFrame[summary]
            sql = "UPDATE treatments SET start_date=" + start_date + ", end_date=" + end_date + ", summary=" + summary + \
                  " WHERE treatment_id=" + treatment_id + ";"
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        with open("treatments.csv", mode='a+', newline='') as file:
            reader = csv.reader(file)
            writer = csv.writer(file)
            for row in reader:
                if row["treatment_id"] == treatment_id:
                    row["start_date"] = start_date if start_date != "" else row["start_date"]
                    row["end_date"] = end_date if end_date != "" else row["end_date"]
                    row["summary"] = summary if summary != "" else row["summary"]
                    writer.writerow(row)
                    break


# DeleteTreatment
def remove_treatment(treatment_id):
    global cursor, db
    if cursor:
        try:
            sql = "DELETE * FROM treatments WHERE treatment_id =" + treatment_id + ";"
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        df = pd.read_csv("treatments.csv")
        df = df[df.treatment_id != treatment_id]
        df.to_csv("treatments.csv", index=False)


# Visit
# VisitID, TreatmentID, Date, Summary, AttentionLevel, ExternalSource


# CreateVisit
def add_visit(visit_name, treatment_id, date, summary="", attention_level="", external_source=""):
    global cursor, db
    if cursor:
        sql = "INSERT INTO visits (visit_name, treatment_id, date, summary, attention_level, external_source) VALUES (%s, %s, %s, %s, %s)"
        val = (treatment_id, date, summary, attention_level, external_source)
        cursor.execute(sql, val)
        db.commit()
    else:
        with open("visits.csv", mode='a+', newline='') as file:
            data = file.readlines()
            new_id = data[-1][0] + 1
            writer = csv.writer(file)
            writer.writerow([new_id, visit_name, treatment_id, date, summary, attention_level, external_source])


# ReadAllVisits
def get_visits(treatment_id):
    global cursor, db
    if cursor:
        try:
            sql = "SELECT * FROM visits WHERE treatment_id=" + treatment_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            return result_dataFrame
        except Exception as e:
            print(str(e))
    else:
        visits = list()
        with open("visits.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[2] == int(treatment_id):
                    visits.append(row)
        return visits


# UpdateVisit
def update_visit(visit_id, date, summary="", attention_level="", external_source=""):
    global cursor, db
    if cursor:
        try:
            sql = "SELECT * FROM visits WHERE visit_id =" + visit_id + ";"
            result_dataFrame = pd.read_sql(sql, cursor)
            date = date if date != "" else result_dataFrame[date]
            summary = summary if summary != "" else result_dataFrame[summary]
            attention_level = attention_level if attention_level != "" else result_dataFrame[attention_level]
            external_source = external_source if external_source != "" else result_dataFrame[external_source]
            sql = "UPDATE treatments SET date=" + date + ", summary=" + summary + ", attention_level=" + attention_level + \
                  ",external_source=" + external_source + \
                  " WHERE visit_id=" + visit_id + ";"
            cursor.execute(sql)
            db.commit()
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
            sql = "DELETE * FROM treatments WHERE visit_id =" + visit_id + ";"
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(str(e))
    else:
        df = pd.read_csv("visits.csv")
        df = df[df.visit_id != visit_id]
        df.to_csv("visits.csv", index=False)
