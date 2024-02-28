import sqlite3


def create_table():
    conn=sqlite3.connect('Pharmacy.db')
    cursor= conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PHARMACY (
            Ref_no INT PRIMARY KEY,
            med_name TEXT,
            company_name TEXT,
            issue_date TEXT,
            expiry_date TEXT,
            classi_name TEXT       
            )''')
    conn.commit()
    conn.close()

def fetch_Pharmacy():
    conn=sqlite3.connect('Pharmacy.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM Pharmacy')
    pharmacy=cursor.fetchall()
    conn.close()
    return pharmacy

def insert_medicine(Ref_no, med_name, company_name, issue_date, expiry_date, classi_name):
    conn= sqlite3.connect('Pharmacy.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO Pharmacy (Ref_no, med_name, company_name, issue_date, expiry_date, classi_name) VALUES (?, ?, ?, ?, ?, ?)',
                   (Ref_no, med_name, company_name, issue_date, expiry_date, classi_name))
    conn.commit()
    conn.close()

def delete_medicine(Ref_no):
    conn= sqlite3.connect('Pharmacy.db')
    cursor=conn.cursor()
    cursor.execute('DELETE FROM Pharmacy WHERE Ref_no = ?', (Ref_no,))
    conn.commit()
    conn.close()

def update_medicine(new_med_name, new_company_name, new_issue_date, new_expiry_date, new_classi_name, Ref_no):
    conn= sqlite3.connect('Pharmacy.db')
    cursor=conn.cursor()
    cursor.execute('UPDATE Pharmacy SET med_name = ?, company_name = ?, issue_date = ?, expiry_date = ?, classi_name = ? WHERE Ref_no = ?', 
                   (new_med_name, new_company_name, new_issue_date, new_expiry_date, new_classi_name, Ref_no))
    conn.commit()
    conn.close()

def Ref_no_exists(Ref_no):
    conn=sqlite3.connect('Pharmacy.db')
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Pharmacy WHERE Ref_No = ?', (Ref_no,))
    result=cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()



