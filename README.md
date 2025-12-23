# Pantry Planner 🥗

Pantry Planner is a full-stack web application that helps users plan meals based on ingredients they already have. The project focuses on clean frontend–backend architecture, RESTful API design, and real-world data synchronization patterns.

---

## Motivation

As a student, I often had ingredients available but no clear idea what meals I could actually make with them. Pantry Planner helps answer questions like:

- *What can I cook with what I already have?*
- *What ingredients am I missing for a recipe?*
- *What should I buy next time I go shopping?*

This project also serves as a hands-on learning experience for building a **production-style full-stack application** with clear separation of concerns between frontend and backend.

---

## Tech Stack

### Frontend
- **React** with Hooks (`useState`, `useEffect`)
- **React Router** for multi-page navigation
- **Axios** for HTTP requests
- HTML / CSS / JavaScript

### Backend
- **Python**
- **FastAPI**
- RESTful API design (CRUD)
- CORS configuration for cross-origin requests

---

## Architecture Overview

This project follows modern full-stack design principles:

- The **backend is the single source of truth** for application data
- The **frontend never mutates data directly**
- All data changes go through REST API endpoints
- After every mutation, the frontend **re-fetches backend truth**
- UI state remains synchronized with backend state at all times

This mirrors real-world production architecture used in industry applications.

---

## Current Features

### Pantry Management
- Add ingredients
- Edit ingredients
- Delete ingredients
- Persistent state while backend is running

### Backend
- RESTful endpoints:
  - `GET /pantry`
  - `POST /pantry`
  - `PUT /pantry/{id}`
  - `DELETE /pantry/{id}`
- Input validation and error handling
- Safe ID generation (no collisions after deletes)
- CORS-enabled for frontend communication

### Frontend
- Clean React state management with immutability
- Centralized API client using Axios
- Full CRUD integration with backend
- Multi-page navigation using React Router

---

## Project Structure
```
pantry-planner/
├── backend/
│   ├── main.py              # FastAPI application
│
├── frontend/
│   ├── src/
│   │   ├── api/             # Axios client
│   │   ├── pages/           # React pages
│   │   └── App.js           # Main application logic
│   └── package.json
└── README.md
```

---

## What I Learned

- Designing a backend as the **authoritative data source**
- Implementing full CRUD with RESTful APIs
- Migrating frontend HTTP logic from Fetch to Axios
- Centralizing API communication for maintainability
- Handling async data flow and error states
- Refactoring working code to improve structure and clarity
- Managing real-world Git workflows (pulling remote changes, clean commits)

---

## Planned Enhancements

- Database integration (SQLite or PostgreSQL)
- Recipe matching based on available ingredients
- Shopping list generation
- Improved UI/UX
- Loading and error states
- Deployment


---

## Running Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
- API available at: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`

### Frontend
```bash
cd frontend
npm install
npm start
```
- App runs at: `http://localhost:3000`

---

## Contact

**Miguel Salvador**  
Computer Science Student | Portland State University

- GitHub: [https://github.com/msalvad2](https://github.com/msalvad2)
- LinkedIn: [https://www.linkedin.com/in/miguel-salvador-4049a528b/](https://www.linkedin.com/in/miguel-salvador-4049a528b/)
