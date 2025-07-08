import mysql.connector as mycnn

def insert_data(first_name, last_name, enrollment):
    try:
        mydb = mycnn.connect(
            host="localhost",
            user="username",
            password="password",
            database="Streamlit_Query"
        )
        
        mycursor = mydb.cursor()
        
        # Use parameterized query to prevent SQL injection
        sql = "INSERT INTO DATA (FirstName, LastName, EnrollmentNo) VALUES (%s, %s, %s)"
        values = (first_name, last_name, enrollment)
        
        mycursor.execute(sql, values)
        mydb.commit()  # Commit the transaction
        print("Data inserted successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'mycursor' in locals():
            mycursor.close()
        if 'mydb' in locals():
            mydb.close()