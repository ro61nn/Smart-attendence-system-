# 🛠️ Setup Guide - AI-Based Smart Attendance System

## Step-by-Step Installation

### 1. Prerequisites
- Python 3.7 or higher
- pip (comes with Python)
- Git (optional, for cloning)

### 2. Project Structure Setup

Your project folder should look like this:
```
attendance-system/
├── app.py
├── index.html
├── db_setup.py
├── requirements.txt
├── README.md
├── SETUP.md
├── .gitignore
└── templates/          (folder - Flask will auto-create)
    └── index.html      (Move index.html here)
```

### 3. Initial Setup

**Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Create Templates Folder**
```bash
mkdir templates
mv index.html templates/index.html
```

**Step 3: Initialize Database**
```bash
python db_setup.py
```

This will create:
- `attendance.db` (SQLite database)
- Tables: users, attendance

**Step 4: Run the Application**
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

**Step 5: Access the Application**
Open your browser and go to: `http://localhost:5000`

## Configuration

### Change Database Location
Edit `app.py`:
```python
DATABASE = 'your_path/attendance.db'
```

### Change Server Port
Edit `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change 5000 to your port
```

### Add Sample Data
Edit `db_setup.py` and uncomment:
```python
if __name__ == '__main__':
    init_database()
    add_sample_data()  # Uncomment this line
    view_database_info()
```

Then run:
```bash
python db_setup.py
```

## Common Issues & Solutions

### Issue 1: Port 5000 Already in Use
**Solution:**
```bash
# On Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On Mac/Linux
lsof -i :5000
kill -9 <PID>
```

### Issue 2: Module Not Found (Flask, Flask-CORS)
**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue 3: Database is Locked
**Solution:**
```bash
rm attendance.db
python db_setup.py
python app.py
```

### Issue 4: HTML Not Loading
**Ensure folder structure:**
- `index.html` should be in `templates/` folder
- Flask looks for templates in the `templates/` directory

### Issue 5: CORS Errors in Console
**Verify in app.py:**
```python
from flask_cors import CORS
CORS(app)  # This should be present
```

## Features to Test

1. **Register User**
   - Go to "Register User" tab
   - Fill in name, email, student ID
   - Click "Register User"

2. **Mark Attendance**
   - Go to "Mark Attendance" tab
   - Select a user
   - Click "Mark Attendance"
   - Check timestamp in records

3. **View Dashboard**
   - Go to "Dashboard" tab
   - See today's statistics
   - Click "Refresh" to update

4. **Generate Reports**
   - Go to "Reports" tab
   - Select a user
   - View their attendance history

## Environment Variables (Optional)

Create a `.env` file for secure configuration:
```
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_PATH=attendance.db
SERVER_PORT=5000
```

Load in `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
DATABASE = os.getenv('DATABASE_PATH', 'attendance.db')
```

Install python-dotenv:
```bash
pip install python-dotenv
```

## Next Steps

### For Local Development
- ✅ Run `python app.py` to start
- ✅ Access `http://localhost:5000`
- ✅ Test all features

### For Deployment
- Change `debug=False` in app.py
- Use production WSGI server (Gunicorn)
- Set up SSL certificate
- Use environment variables for secrets

### For GitHub
1. Create repository
2. Add these files
3. Commit and push
4. Update README with your GitHub URL

```bash
git init
git add .
git commit -m "Initial commit: AI Attendance System"
git branch -M main
git remote add origin https://github.com/yourusername/attendance-system.git
git push -u origin main
```

## Production Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Heroku
```bash
# Install Heroku CLI
heroku login
heroku create your-app-name
git push heroku main
```

### Using PythonAnywhere
1. Upload files
2. Set up virtual environment
3. Configure WSGI file
4. Enable website

## Support

If you encounter issues:
1. Check the README.md
2. Review error messages in console
3. Ensure all files are in correct locations
4. Verify Python and pip versions

---

**Happy coding! 🚀**
