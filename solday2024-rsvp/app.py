from flask import Flask, render_template, request, redirect
import mysql.connector
import os
import logging

app = Flask(__name__)

# Mengambil konfigurasi database dari variabel lingkungan
db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE'),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rsvp (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "There was an issue connecting to the database."

        return redirect('/')
    
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM rsvp")
        rsvps = cursor.fetchall()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        rsvps = []

    return render_template('index.html', rsvps=rsvps)

@app.route('/delete/<int:rsvp_id>', methods=['POST'])
def delete_rsvp(rsvp_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rsvp WHERE id = %s", (rsvp_id,))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "There was an issue connecting to the database."

    return redirect('/')

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

