from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import os
import time

app = FastAPI(title="DevOps Capstone API", version="1.0.0")

# Database connection helper
def get_db_connection():
    db_host = os.getenv("DB_HOST", "localhost")
    db_name = os.getenv("DB_NAME", "capstone")
    db_user = os.getenv("DB_USER", "postgres")
    db_pass = os.getenv("DB_PASSWORD", "postgres123")
    db_port = os.getenv("DB_PORT", "5432")
    
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass,
        port=db_port,
        cursor_factory=RealDictCursor
    )
    return conn

class TaskItem(BaseModel):
    title: str
    description: str

@app.get("/")
def read_root():
    return {"message": "DevOps Capstone API is Operational", "timestamp": time.time()}

@app.get("/healthz")
def healthcheck():
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
        conn.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database unreachable: {str(e)}")

@app.get("/metrics")
def metrics():
    # Basic Prometheus exposition format
    return "# HELP http_requests_total Total number of requests\n# TYPE http_requests_total counter\nhttp_requests_total 42\n"

@app.get("/api/v1/tasks")
def list_tasks():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, title, description, created_at FROM tasks ORDER BY created_at DESC;")
        rows = cur.fetchall()
    conn.close()
    return {"tasks": rows}

@app.post("/api/v1/tasks", status_code=201)
def create_task(task: TaskItem):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING id, title, description, created_at;",
            (task.title, task.description)
        )
        new_task = cur.fetchone()
        conn.commit()
    conn.close()
    return {"task": new_task}
