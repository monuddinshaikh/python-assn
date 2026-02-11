import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()

# Create table (SQLite syntax)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

print("Database and table created successfully")

# Insert data
cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Rahul", 20, "Python"))

cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
               ("Anita", 22, "Data Science"))

conn.commit()
print("Data inserted successfully")

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

# Close connection
conn.close()
