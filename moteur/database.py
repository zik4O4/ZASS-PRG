import csv
import os
import sqlite3
import webbrowser

conn =sqlite3.connect("ziko.db")
curs= conn.cursor()

# code="CREATE TABLE IF NOT EXISTS system_commend (ID INTEGER PRIMARY KEY,NAME VARCHAR(100),URL VARCHAR(100))"
# curs.execute(code)


# code="CREATE TABLE IF NOT EXISTS web_commend (ID INTEGER PRIMARY KEY,NAME VARCHAR(100),URL VARCHAR(100))"
# curs.execute(code)

# code="INSERT INTO system_commend (NAME, URL)  VALUES('Control Panel', 'C:\\Users\\ziko\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.exe')"
# curs.execute(code)
# conn.commit()

# code="INSERT INTO web_commend (NAME, URL)  VALUES('youtube', 'https://youtube.com/')"
# curs.execute(code)
# conn.commit()


# code="ALTER TABLE system_commend RENAME COLUMN URL TO PATH"
# curs.execute(code)
# conn.commit()

# code="UPDATE system_commend SET PATH ='C:\Windows\System32\control.exe' WHERE NAME ='Control Panel'"
# curs.execute(code)
# conn.commit()

# code="DELETE FROM system_commend WHERE ID =3 OR ID=2"
# curs.execute(code)
# conn.commit()

# apk_name= "Control Panel"
# curs.execute('SELECT PATH FROM system_commend WHERE NAME IN (?)', (apk_name,))
# results = curs.fetchall()
# os.startfile(results[0][0])
# print(results[0][0])


# apk_name= "YouTube"
# apk_name=apk_name.lower()
# curs.execute('SELECT URL FROM web_commend WHERE NAME IN (?)', (apk_name,))
# results = curs.fetchall()
# webbrowser.open(results[0][0])
# print(results[0][0])

# Create a table with the desired columns
# curs.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 30]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         curs.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()




####  Insert Single contacts (Optional)

# code = "INSERT INTO contacts (name,mobile_no) VALUES ('mom', '+212624136272')"
# curs.execute(code)
# conn.commit()

