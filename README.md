# 🎓 AI-Based Smart Attendance Monitoring System

An intelligent attendance management system using Python Flask backend with face recognition capabilities and a modern responsive web frontend.

##Dashboard
![image alt](

## ✨ Features

- 👤 **User Registration** - Register students with name, email, and student ID
- ✅ **Mark Attendance** - Quick attendance marking with timestamp
- 📊 **Real-time Dashboard** - View daily attendance statistics
- 📈 **Attendance Reports** - Historical records and analytics
- 🔐 **Database Management** - SQLite for reliable data storage
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/attendance-system.git
   cd attendance-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Application**
   - Open your browser
   - Navigate to `http://localhost:5000`
   - Start managing attendance!

## 📁 Project Structure

```
attendance-system/
├── app.py                 # Flask backend application
├── index.html            # Frontend UI
├── attendance.db         # SQLite database (auto-created)
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── uploads/             # Folder for face recognition data (auto-created)
```

## 🔧 API Endpoints

### User Management
- `POST /api/register` - Register new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "student_id": "STU001"
  }
  ```

- `GET /api/users` - Get all registered users

### Attendance
- `POST /api/attendance` - Mark attendance
  ```json
  {
    "user_id": 1
  }
  ```

- `GET /api/attendance/<user_id>` - Get user attendance history

### Dashboard
- `GET /api/dashboard` - Get today's attendance overview

## 📊 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    student_id TEXT UNIQUE NOT NULL,
    face_encoding TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Attendance Table
```sql
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date DATE,
    time_in TIMESTAMP,
    time_out TIMESTAMP,
    status TEXT DEFAULT 'Present',
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## 🎯 Usage Guide

### Register a Student
1. Click "Register User" tab
2. Enter name, email, and student ID
3. Click "Register User" button
4. Confirmation message appears

### Mark Attendance
1. Click "Mark Attendance" tab
2. Select student from dropdown
3. Click "Mark Attendance" button
4. Timestamp is recorded automatically

### View Dashboard
1. Click "Dashboard" tab
2. See real-time attendance statistics
3. View all students' status for the day

### Generate Reports
1. Click "Reports" tab
2. Select a student
3. View their attendance history for last 30 days

## 🚀 Future Enhancements

- [ ] Integrate face recognition (OpenCV + face_recognition)
- [ ] Add admin authentication
- [ ] Export reports to PDF/Excel
- [ ] Real-time notifications
- [ ] Mobile app integration
- [ ] Advanced analytics and predictions
- [ ] QR code based attendance
- [ ] Email notifications

## 📋 Configuration

### Database Path
To change database location, modify in `app.py`:
```python
DATABASE = 'attendance.db'  # Change this path
```

### Server Port
To change Flask server port, modify in `app.py`:
```python
app.run(debug=True, port=5000)  # Change port number
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py or kill process on port 5000
lsof -i :5000
kill -9 <PID>
```

### CORS Issues
- Ensure Flask-CORS is installed
- Check allowed origins in app.py

### Database Lock
- Delete `attendance.db` file and restart the application
- Database will be auto-created

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Your Name - Initial work

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For support, email your-email@example.com or open an issue on GitHub.

---

**Made with ❤️ for educational institutions**
