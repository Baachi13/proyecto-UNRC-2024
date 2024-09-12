import sqlite3
from datetime import datetime

def connect():
    try:
        conn = sqlite3.connect('db/database.db')
        
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def insert_patient(dni, firstName, lastName, password, email, phoneNumber, dateBirth, nationality, province,
                   locality, postalCode, address, gender, imagePatient=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO patient (dni, firstName, lastName, password, email, phoneNumber, dateBirth, age, nationality, province, 
                   locality, postalCode, address, gender, imagePatient) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (dni, firstName, lastName, password, email, phoneNumber, dateBirth, calculate_age(dateBirth),
                    nationality, province,
                    locality, postalCode, address, gender, imagePatient))

    conn.commit()
    conn.close()


def delete_patient(dni):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM patient WHERE dni = ?", (dni,))
    print(f"patient with DNI {dni} successfully removed")
    
    conn.commit()
    conn.close()

#Faltaria arreglar que si se elimina un paciente se deberian eliminar sus diagnosticos correspondientes
#Ya esta hecho con la foreign key!!


def get_patient(dni):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patient WHERE dni = ?", (dni,))
    patient_data = cursor.fetchone()

    conn.close()
    return patient_data


def modify_password(dni, newPassword):
    conn = connect()
    cursor = conn.cursor()

    query = """UPDATE patient 
            SET password = ? 
            WHERE dni = ?"""
    cursor.execute(query, (newPassword, dni))

    conn.commit()
    conn.close()

def modify_image_patient(dni, imagePatient):
    conn = connect()
    cursor = conn.cursor()

    query = """UPDATE patient
            SET imagePatient = ?
            WHERE dni = ?"""
    cursor.execute(query, (imagePatient, dni))

    conn.commit()
    conn.close()

def modify_patient(dni, firstName, lastName, email, phoneNumber, dateBirth, nationality, province, locality, postalCode, address, gender, imagePatient=None):
    conn = connect()
    cursor = conn.cursor()
    print(f"Updating gender to: {gender}")  # Agrega esto para depuración
    query = """
        UPDATE patient 
        SET firstName = ?, lastName = ?, email = ?, phoneNumber = ?, dateBirth = ?, 
            age = ?, nationality = ?, province = ?, locality = ?, postalCode = ?, address = ?, gender = ?, imagePatient = ?
        WHERE dni = ?
    """
    cursor.execute(query, (firstName, lastName, email, phoneNumber, dateBirth, calculate_age(dateBirth), nationality, province, locality, postalCode, address, gender, imagePatient, dni))

    conn.commit()
    conn.close()



def get_password(dni):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM patient WHERE dni = (?)", (dni,))
    password_data = cursor.fetchone()

    conn.close()
    return password_data[0]


def calculate_age(dateBirth):
    today = datetime.today()
    birth_date = datetime.strptime(dateBirth, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def insert_diagnostic(cod, result, description, imageDiagnostic, dni):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO diagnostic (cod, result, description, imageDiagnostic,dni) VALUES 
                  (?,?,?,?,?,?)""", (cod, result, description, imageDiagnostic, dni))

    conn.commit()
    conn.close()


def get_diagnostics(dni):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diagnostic WHERE dni = ?", (dni,))
    patient_data = cursor.fetchall()

    conn.commit()
    conn.close()
    return patient_data

def get_diagnostics_by_code(cod):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diagnostic WHERE cod = ?", (cod,))
    patient_data = cursor.fetchall()

    conn.commit()
    conn.close()
    return patient_data

def get_diagnostics_by_result(dni, result):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diagnostic WHERE (dni,result) = (?,?)", (dni, result))
    patient_data = cursor.fetchall()

    conn.commit()
    conn.close()
    return patient_data

def get_diagnostics_by_description(dni, description):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM diagnostic WHERE (dni,description) = (?,?) ", (dni, description))
    patient_data = cursor.fetchall()
    
    conn.commit()
    conn.close()
    return patient_data

def insert_doctor(dni,matricule, firstName, lastName, email, phoneNumber, dateBirth, gender, imageDoctor=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO doctor (dni, matricule, firstName, lastName, email, phoneNumber, dateBirth, age, gender, imageDoctor) 
                  VALUES (?,?,?,?,?,?,?,?,?,?)""", 
               (dni, matricule, firstName, lastName, email, phoneNumber, dateBirth, calculate_age(dateBirth), gender, imageDoctor))

    conn.commit()
    conn.close()


def delete_doctor(dni):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM doctor WHERE dni = ?", (dni,))
    print(f"doctor with DNI {dni} successfully removed")
    
    conn.commit()
    conn.close()

def modify_doctor(dni,matricule, firstName, lastName, email, phoneNumber, dateBirth, gender, imageDoctor=None):
    conn = connect()
    cursor = conn.cursor()

    query = """
        UPDATE doctor 
        SET matricule = ?, firstName = ?, lastName = ?, email = ?, phoneNumber = ?, dateBirth = ?, 
            age = ?, gender = ?, imageDoctor = ?
        WHERE dni = ?
    """
    cursor.execute(query, (matricule,firstName, lastName, email, phoneNumber, dateBirth, calculate_age(dateBirth),gender, imageDoctor, dni))

    conn.commit()
    conn.close()

def insert_clinic(name, phoneNumber, province, city, postalCode, address):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO clinic (Name, phoneNumber, province, city, postalCode, address) 
                      VALUES (?, ?, ?, ?, ?, ?)""",
                   (name, phoneNumber, province, city, postalCode, address))

    conn.commit()
    conn.close()