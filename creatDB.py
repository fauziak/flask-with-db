# import sqlite3
from sqlalchemy import create_engine

db_uri = "sqlite:///patients.db"
eng = create_engine(db_uri)
# from turtle import up
# conn = sqlite3.connect('patients.db')
# print(conn, "Opened database successfully")
eng.execute('CREATE TABLE patients(MRN TEXT NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, DOB TEXT NOT NULL, age INT NOT NULL, gender TEXT NOT NULL, address TEXT NOT NULL, type_of_visit TEXT NOT NULL)')
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('FK72cD', 'Rachel', 'Charles','10/07/1999','22','F','982 Maple Rd. Upland, CA 91784', 'Follow-up')")
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('MK32dJ', 'Ross', 'John','11/11/2000','21','M','767 San Juan St.Loveland, OH 45140', 'New Patient')")
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('JU76d4', 'Chandler', 'Fisher','12/03/1997','24','M','8623 Ashley LaneBaton Rouge, LA 70806','Post-Op')")
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('KP98g6', 'Joey', 'Fields','01/06/1998','24','M','658 North Marvon StreetSolon, OH 44139', 'New patient')")
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('EB20j7', 'Monica', 'Benson','05/09/2006','16','F','254 Oxford St.Dallas, GA 30132', 'Labs')")
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('HQ50x5', 'Phoebe', 'Hastings','09/27/2000','22','F','360 Briarwood St.Union, NJ 07083', 'Follow-up')")
eng.execute("INSERT INTO patients(MRN, first_name, last_name, DOB, age, gender, address, type_of_visit) values('AM83na', 'Gunther', 'Fitz','03/08/1998','24','M','22 East Virginia Ave.Elgin, IL 601204', 'Post-Op')")
