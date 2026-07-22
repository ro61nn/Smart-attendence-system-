from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Database setup
DATABASE = 'attendance.db'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            student_id TEXT UNIQUE NOT NULL,
            face_encoding TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date DATE,
            time_in TIMESTAMP,
            time_out TIMESTAMP,
            status TEXT DEFAULT 'Present',
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
if not os.path.exists(DATABASE):
    init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        student_id = data.get('student_id')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, student_id) VALUES (?, ?, ?)',
                      (name, email, student_id))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        
        return jsonify({'success': True, 'user_id': user_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'error': 'User already exists'}), 400

@app.route('/api/attendance', methods=['POST'])
def mark_attendance():
    try:
        data = request.json
        user_id = data.get('user_id')
        
        conn = get_db()
        cursor = conn.cursor()
        today = datetime.now().date()
        
        # Check if already marked
        cursor.execute('SELECT id FROM attendance WHERE user_id = ? AND date = ?',
                      (user_id, today))
        existing = cursor.fetchone()
        
        if existing:
            cursor.execute('UPDATE attendance SET time_out = ? WHERE id = ?',
                          (datetime.now(), existing['id']))
        else:
            cursor.execute('INSERT INTO attendance (user_id, date, time_in, status) VALUES (?, ?, ?, ?)',
                          (user_id, today, datetime.now(), 'Present'))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Attendance marked'}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/attendance/<int:user_id>', methods=['GET'])
def get_attendance(user_id):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT a.date, a.time_in, a.time_out, a.status, u.name 
            FROM attendance a 
            JOIN users u ON a.user_id = u.id 
            WHERE a.user_id = ? 
            ORDER BY a.date DESC LIMIT 30
        ''', (user_id,))
        records = cursor.fetchall()
        conn.close()
        
        return jsonify({'success': True, 'records': [dict(r) for r in records]}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, student_id FROM users')
        users = cursor.fetchall()
        conn.close()
        
        return jsonify({'success': True, 'users': [dict(u) for u in users]}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    try:
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) as total_users FROM users')
        total_users = cursor.fetchone()['total_users']
        
        cursor.execute('SELECT COUNT(*) as total_present FROM attendance WHERE status = "Present" AND date = DATE("now")')
        today_present = cursor.fetchone()['total_present']
        
        cursor.execute('''
            SELECT u.id, u.name, u.student_id, 
            CASE WHEN a.date = DATE("now") THEN "Present" ELSE "Absent" END as status
            FROM users u
            LEFT JOIN attendance a ON u.id = a.user_id AND a.date = DATE("now")
            ORDER BY u.name
        ''')
        today_report = cursor.fetchall()
        
        conn.close()
        
        return jsonify({
            'success': True,
            'total_users': total_users,
            'today_present': today_present,
            'today_absent': total_users - today_present,
            'report': [dict(r) for r in today_report]
        }), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
