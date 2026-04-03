# 📝 Fullstack Task Manager

A high-performance Task Management application built with a **FastAPI** backend, **PostgreSQL** database, and **Vue.js 3** frontend — all running natively in WSL (Ubuntu 22.04).

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, FastAPI, SQLAlchemy (ORM) |
| **Database** | PostgreSQL 14+ |
| **Frontend** | Vue.js 3 (Composition API), Vite |
| **Environment** | Windows Subsystem for Linux (WSL2) |

---

## 🛠️ Prerequisites

Ensure you have the following installed inside your **Ubuntu (WSL) terminal**:

```bash
# Python 3 & virtual environment support
sudo apt install python3-venv

# Node.js & NPM
sudo apt install nodejs npm

# PostgreSQL
sudo apt install postgresql postgresql-contrib
```

---

## 🐘 1. Database Setup

**Start the PostgreSQL service:**

```bash
sudo service postgresql start
```

**Create a dedicated user and database:**

```bash
sudo -u postgres psql
```

Inside the `psql` shell:

```sql
CREATE USER balaji_dev WITH PASSWORD 'your_password';
CREATE DATABASE my_app_db OWNER balaji_dev;
\q
```

---

## 🐍 2. Backend — Installation & Run

**Navigate to the backend folder:**

```bash
cd backend
```

**Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Configure environment variables:**

Create a `.env` file inside the `backend/` folder:

```env
DATABASE_URL=postgresql://balaji_dev:your_password@localhost:5432/my_app_db
```

**Start the API server:**

```bash
uvicorn main:app --reload
```

> 📖 Interactive API docs available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ⚡ 3. Frontend — Installation & Run

**Open a new terminal tab and navigate to the frontend folder:**

```bash
cd frontend
```

**Install NPM packages:**

```bash
npm install
```

**Launch the development server:**

```bash
npm run dev
```

> 🌐 Frontend available at: [http://localhost:5173](http://localhost:5173)

---

## 📂 Project Structure

```
my-app/
├── backend/            # FastAPI project
│   ├── venv/           # Python virtual environment
│   ├── main.py         # API routes & logic
│   ├── models.py       # SQLAlchemy models
│   └── database.py     # Database connection logic
└── frontend/           # Vue.js project
    ├── src/            # Vue components & views
    └── package.json    # JS dependencies
```

---

## 🛡️ Security Notes

- The `.env` file is listed in `.gitignore` to prevent accidental exposure of database credentials.
- CORS is configured in `main.py` to allow communication between the Vite dev server (`localhost:5173`) and the FastAPI backend (`localhost:8000`).

---

## 🚀 Quick Start Summary

```bash
# 1. Start the database
sudo service postgresql start

# 2. Run the backend (in one terminal)
cd backend && source venv/bin/activate && uvicorn main:app --reload

# 3. Run the frontend (in another terminal)
cd frontend && npm run dev
```