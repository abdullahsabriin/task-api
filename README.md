# Task API (FastAPI + AWS)

A backend API built using FastAPI and SQLAlchemy, deployed on AWS EC2.

---

## Live Demo
http://51.20.89.236:8000/docs

---

## Features
- Get tasks
- Add tasks
- Delete tasks

---

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- AWS EC2
- Uvicorn

---

## API Endpoints

GET /tasks  
POST /tasks  
DELETE /tasks/{task_id}

---

## Example

POST /tasks?title=Learn FastAPI

Response:
{
  "id": 1,
  "title": "Learn FastAPI"
}

---

## Project Structure

api.py → main API  
tasks.db → database  
requirements.txt → dependencies  

---

## Why this project

This project was built to practice backend development concepts including API design, database integration, and deploying applications on AWS EC2.
