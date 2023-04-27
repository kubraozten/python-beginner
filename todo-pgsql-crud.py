import psycopg2
import traceback

def connect():
    try:
            connection = psycopg2.connect(
            host="localhost",
            database="todo",
            user="postgres",
            password="postgres"
            )
            return connection
    except Exception as err:
        print('Error occurred in making connection …')
        traceback.print_exc()

def print_version(connection):
    cursor = connect().cursor()
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(db_version)
    cursor.close()
    connection.close()

def create(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""CREATE TABLE todolist(
                             id INTEGER PRIMARY KEY,
                             todo_text VARCHAR(100)
                             )
                       """)
        connection.commit()
        print("table created successfully!")
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()

def insert(connection):
    cursor = connection.cursor()
    query = """
    INSERT INTO todolist (id, todo_text) VALUES (%s, %s);
    """
    try:
        data = (1, "Buy Book")
        cursor.execute(query, data)
        connection.commit()
        print("Record inserted successfully!")
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()

def read(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM todolist LIMIT 500;")
        record = cursor.fetchone()
        print(f"Read successful, 1st row is : id = {record[0]}, todo= {record[1]}")
        connection.commit()
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()

def update(connection):
    cursor = connection.cursor()
    query = """
    UPDATE todolist  SET todo_text= %s WHERE id=%s;
    """
    try:
        cursor.execute(query, ("Send Email", 1))
        cursor.execute("SELECT * FROM todolist  WHERE id=1;")
        record = cursor.fetchone()
        print(f"Update successful : id = {record[0]}, todo= {record[1]}")
        connection.commit()
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()

def delete(connection):
    cursor = connection.cursor()
    query = """
    DELETE FROM todolist WHERE id=1;
    """
    try:
        cursor.execute(query)
        cursor.execute("select * from todolist;")
        record = cursor.fetchone()
        print(record)
        connection.commit()
    except Exception as err:
        print(err)
    cursor.close()
    connection.close()

    

if __name__ == "__main__":
    print_version(connect())
    #create(connect())
    #insert(connect())
    read(connect())
    #update(connect())
