from flask import Flask, request, Response,render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ttmokoane7?!',
    'database': 'Software_Data'
}
@app.route('/Nodeone', methods=['POST'])
def Nodeone():
    data = request.get_json()

    if data is None or 'light_intensity' not in data or 'User_Id' not in data:
        error_response = Response(
            response='{"error": "Missing or invalid JSON"}',
            status=400,
            mimetype='application/json'
        )
        return error_response

    user_id = data['User_Id']
    light_intensity = data['light_intensity']

    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Node_1 (User_Id, light_intensity) VALUES (%s, %s)", (user_id, light_intensity))
            connection.commit()
            cursor.close()
            connection.close()
            success_response = Response(
                response='{"message": "Data added successfully"}',
                status=201,
                mimetype='application/json'
            )
            return success_response

    except Error as e:
        error_response = Response(
            response='{"error": "' + str(e) + '"}',
            status=500,
            mimetype='application/json'
        )
        return error_response

    unknown_error_response = Response(
        response='{"error": "Unknown error"}',
        status=500,
        mimetype='application/json'
    )
    return unknown_error_response

@app.route('/add_dataNodetwo', methods=['POST'])
def add_dataNodetwo():
    data = request.get_json()

    if data is None or 'light_intensity' not in data or 'User_Id' not in data:
        error_response = Response(
            response='{"error": "Missing or invalid JSON"}',
            status=400,
            mimetype='application/json'
        )
        return error_response

    user_id = data['User_Id']
    light_intensity = data['light_intensity']

    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Node_2 (User_Id, light_intensity) VALUES (%s, %s)", (user_id, light_intensity))
            connection.commit()
            cursor.close()
            connection.close()
            success_response = Response(
                response='{"message": "Data added successfully"}',
                status=201,
                mimetype='application/json'
            )
            return success_response

    except Error as e:
        error_response = Response(
            response='{"error": "' + str(e) + '"}',
            status=500,
            mimetype='application/json'
        )
        return error_response

    unknown_error_response = Response(
        response='{"error": "Unknown error"}',
        status=500,
        mimetype='application/json'
    )
    return unknown_error_response
@app.route('/Nodethhree', methods=['POST'])
def Nodethhree():
    data = request.get_json()

    if data is None or 'light_intensity' not in data or 'User_Id' not in data:
        error_response = Response(
            response='{"error": "Missing or invalid JSON"}',
            status=400,
            mimetype='application/json'
        )
        return error_response

    user_id = data['User_Id']
    light_intensity = data['light_intensity']

    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Node_3 (User_Id, light_intensity) VALUES (%s, %s)", (user_id, light_intensity))
            connection.commit()
            cursor.close()
            connection.close()
            success_response = Response(
                response='{"message": "Data added successfully"}',
                status=201,
                mimetype='application/json'
            )
            return success_response

    except Error as e:
        error_response = Response(
            response='{"error": "' + str(e) + '"}',
            status=500,
            mimetype='application/json'
        )
        return error_response

    unknown_error_response = Response(
        response='{"error": "Unknown error"}',
        status=500,
        mimetype='application/json'
    )
    return unknown_error_response

def check_user(User_Id, User_Pass):
    connection = mysql.connector.connect(**db_config)
    cursor = connection .cursor()
    cursor.execute("SELECT User_Id, User_Pass FROM Users WHERE User_Id = %s AND User_Pass = %s", (User_Id, User_Pass))
    user = cursor.fetchone()
    connection .close()
    return user
def check_Node1 (User_Id, User_Pass):
    connection = mysql.connector.connect(**db_config)
    cursor = connection .cursor()
    cursor.execute("SELECT * FROM Users WHERE User_Id = 221967575 AND User_Pass = %s", (User_Pass,))
    Node1 = cursor.fetchone()
    connection .close()
    return Node1

def check_Node2 (User_Id, User_Pass):
    connection = mysql.connector.connect(**db_config)
    cursor = connection .cursor()
    cursor.execute("SELECT * FROM Users WHERE User_Id = 221802177 AND User_Pass = %s", (User_Pass,))
    Node2 = cursor.fetchone()
    connection .close()
    return Node2

def check_Node3 (User_Id, User_Pass):
    connection = mysql.connector.connect(**db_config)
    cursor = connection .cursor()
    cursor.execute("SELECT * FROM Users WHERE User_Id = 215410599 AND User_Pass = %s", (User_Pass,))
    Node3 = cursor.fetchone()
    connection .close()
    return Node3

def check_Node4 (User_Id, User_Pass):
    connection = mysql.connector.connect(**db_config)
    cursor = connection .cursor()
    cursor.execute("SELECT * FROM Users WHERE User_Id = 221130195 AND User_Pass = %s", (User_Pass,))
    Node4 = cursor.fetchone()
    connection .close()
    return Node4
# Function to sign up a user
def signup_user(User_Id, User_Pass, User_Name, User_Surname):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = """
        INSERT INTO Users (User_Id, User_Pass, User_Name, User_Surname)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (User_Id, User_Pass, User_Name, User_Surname))
        connection.commit()
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    


@app.route("/")
def home():
    return render_template("homeB.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        user_pass = request.form['password']

        
        node1 = check_Node1(user_id, user_pass)
        node2 = check_Node2(user_id, user_pass)
        node3 = check_Node3(user_id, user_pass)
        node4 = check_Node4(user_id, user_pass)
        admin = checkAdmin(user_id, user_pass)

        if node1:
            return redirect(url_for('node_1'))
        elif node2:
            return redirect(url_for('node_2'))
        elif node3:
            return redirect(url_for('node_3'))
        elif node4:
            return redirect(url_for('node_4'))
        elif admin:
            return redirect(url_for('adminsecpage'))
            
        else:   
            return redirect(url_for('register'))
    else:
        return render_template('login.html') 


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        User_Id = request.form['username']
        User_Pass = request.form['password']
        User_Name = request.form['name']
        User_Surname = request.form['surname']

        signup_user(User_Id, User_Pass, User_Name, User_Surname)
        message = "registration succesful now Enter login details to access the system"
        return redirect(url_for('secondpage',message=message))
    return render_template('register.html')

def fetch_last_10_rows(table_name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    query = f'SELECT * FROM {table_name} ORDER BY timestamp DESC LIMIT 10'
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/node_1")
def node_1():
    rows = fetch_last_10_rows('Node_1')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT timestamp, light_intensity FROM Node_1 ORDER BY timestamp')
    results = cursor.fetchall()
    conn.close()

    timestamps = [row['timestamp'] for row in results]
    light_intensities = [row['light_intensity'] for row in results]
    return render_template("node_1.html" ,timestamps=timestamps, light_intensities=light_intensities, title="Node 1 Data", rows=rows)

@app.route("/node_2")
def node_2():
    rows = fetch_last_10_rows('Node_2')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT timestamp, light_intensity FROM Node_2 ORDER BY timestamp')
    results = cursor.fetchall()
    conn.close()

    timestamps = [row['timestamp'] for row in results]
    light_intensities = [row['light_intensity'] for row in results]
    return render_template("node_2.html" ,timestamps=timestamps, light_intensities=light_intensities, title="Node 2 Data", rows=rows)

@app.route("/node_3")
def node_3():
    rows = fetch_last_10_rows('Node_3')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT timestamp, light_intensity FROM Node_3 ORDER BY timestamp')
    results = cursor.fetchall()
    conn.close()

    timestamps = [row['timestamp'] for row in results]
    light_intensities = [row['light_intensity'] for row in results]
    return render_template("node_3.html" ,timestamps=timestamps, light_intensities=light_intensities,title="Node 3 Data", rows=rows)

@app.route("/node_4")
def node_4():
    rows = fetch_last_10_rows('Node_4')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT timestamp, light_intensity FROM Node_4 ORDER BY timestamp')
    results = cursor.fetchall()
    conn.close()

    timestamps = [row['timestamp'] for row in results]
    light_intensities = [row['light_intensity'] for row in results]
    return render_template("node_4.html" ,timestamps=timestamps, light_intensities=light_intensities, title="Node 4 Data", rows=rows)

@app.route("/adminsecpage", methods=['GET', 'POST'])
def adminsecpage():
    return render_template("adminsecpage.html")

def checkAdmin(user_id, user_pass):
    if user_id == '1234' and user_pass == 'admin':
        return True
    return False

        
   
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
