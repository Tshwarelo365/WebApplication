from flask import Flask, request, Response,render_template, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ttmokoane7?!',
    'database': 'Software_Data'
}

@app.route('/add_data', methods=['POST'])
def add_data():
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
@app.route('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
                user = cursor.fetchone()
                cursor.close()
                connection.close()
                
                if user:
                    session['user_id'] = user['User_Id']
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid username or password')
                    return redirect(url_for('login'))

        except Error as e:
            flash('Database connection error: ' + str(e))
            return redirect(url_for('login'))

    return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
