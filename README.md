📝 Fullstack Task Manager
A high-performance Task Management application built with a FastAPI backend, PostgreSQL database, and Vue.js 3 frontend, all running natively in WSL (Ubuntu 22.04).

🏗️ Tech Stack
Backend: Python 3.10+, FastAPI, SQLAlchemy (ORM)

Database: PostgreSQL 14+

Frontend: Vue.js 3 (Composition API), Vite

Environment: Windows Subsystem for Linux (WSL2)

🛠️ Prerequisites
Ensure you have the following installed in your Ubuntu terminal:

Python 3 & venv: sudo apt install python3-venv

Node.js & NPM: sudo apt install nodejs npm

PostgreSQL: sudo apt install postgresql postgresql-contrib

🐘 1. Database Setup
Start PostgreSQL service:

Bash
sudo service postgresql start
Create a dedicated user and database:

Bash
sudo -u postgres psql
# Inside psql:
CREATE USER balaji_dev WITH PASSWORD 'your_password';
CREATE DATABASE my_app_db OWNER balaji_dev;
\q
🐍 2. Backend Installation & Run
Navigate to backend folder:

Bash
cd backend
Create and activate Virtual Environment:

Bash
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables:
Create a .env file in the backend/ folder:

Plaintext
DATABASE_URL=postgresql://balaji_dev:your_password@localhost:5432/my_app_db
Run the API:

Bash
uvicorn main:app --reload
API Documentation available at: http://localhost:8000/docs

⚡ 3. Frontend Installation & Run
Open a new terminal tab and navigate to frontend:

Bash
cd frontend
Install NPM packages:

Bash
npm install
Launch Dev Server:

Bash
npm run dev
Frontend available at: http://localhost:5173

🛡️ Security Notes
The .env file is included in .gitignore to prevent leaking database credentials.

CORS is configured in main.py to allow communication between the Vite dev server and the FastAPI backend.

📂 Project Structure
Plaintext
my-app/
├── backend/            # FastAPI Project
│   ├── venv/           # Python Virtual Env
│   ├── main.py         # API Routes & Logic
│   ├── models.py       # SQLAlchemy Models
│   └── database.py     # DB Connection Logic
└── frontend/           # Vue.js Project
    ├── src/            # Vue Components
    └── package.json    # JS Dependencies