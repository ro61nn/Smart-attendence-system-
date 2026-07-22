import sqlite3
import os

DATABASE = 'attendance.db'

def init_database():
    """Initialize the database with required tables"""
    
    # Check if database already exists
    db_exists = os.path.exists(DATABASE)
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create Users Table
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
    
    # Create Attendance Table
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
    
    if not db_exists:
        print(f"✅ Database '{DATABASE}' created successfully!")
        print("📊 Tables created:")
        print("   - users")
        print("   - attendance")
    else:
        print(f"✅ Database '{DATABASE}' already exists and is properly configured!")

def add_sample_data():
    """Add sample users for testing (optional)"""
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    sample_users = [
        ('Alice Johnson', 'alice@example.com', 'STU001'),
        ('Bob Smith', 'bob@example.com', 'STU002'),
        ('Charlie Brown', 'charlie@example.com', 'STU003'),
        ('Diana Prince', 'diana@example.com', 'STU004'),
        ('Eve Wilson', 'eve@example.com', 'STU005'),
    ]
    
    try:
        for name, email, student_id in sample_users:
            cursor.execute(
                'INSERT INTO users (name, email, student_id) VALUES (?, ?, ?)',
                (name, email, student_id)
            )
        conn.commit()
        print("\n✨ Sample data added successfully!")
        print("Sample Users:")
        for name, email, student_id in sample_users:
            print(f"   - {name} ({student_id})")
    except sqlite3.IntegrityError:
        print("\n⚠️  Sample data already exists or duplicate entries found.")
    finally:
        conn.close()

def view_database_info():
    """Display database information"""
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Count users
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    
    # Count attendance records
    cursor.execute('SELECT COUNT(*) FROM attendance')
    attendance_count = cursor.fetchone()[0]
    
    print("\n📊 Database Information:")
    print(f"   Total Users: {user_count}")
    print(f"   Total Attendance Records: {attendance_count}")
    
    # List all users
    cursor.execute('SELECT id, name, student_id FROM users')
    users = cursor.fetchall()
    if users:
        print("\n👥 Registered Users:")
        for user_id, name, student_id in users:
            print(f"   ID {user_id}: {name} ({student_id})")
    
    conn.close()

def reset_database():
    """Reset and recreate the database"""
    
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print(f"🔄 Database '{DATABASE}' has been reset.")
    
    init_database()
    print("✅ Fresh database initialized!")

if __name__ == '__main__':
    print("🎓 AI-Based Smart Attendance System - Database Setup")
    print("=" * 50)
    
    # Initialize database
    init_database()
    
    # Display current info
    view_database_info()
    
    print("\n" + "=" * 50)
    print("💡 To add sample data, modify this script:")
    print("   - Uncomment: add_sample_data()")
    print("   - Save and run: python db_setup.py")
    print("\n✅ Database is ready! Start the app with: python app.py")
