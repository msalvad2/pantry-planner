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
- **SQLAlchemy ORM**
- **SQLite database**
- RESTful API design (CRUD)
- CORS configuration

---

## Architecture Overview

This project follows modern full-stack design principles:

- The **backend is the single source of truth** for application data
- The **frontend never mutates data directly**
- All data changes go through REST API endpoints
- After every mutation, the frontend **re-fetches backend truth**
- UI state always reflects the database

This mirrors real-world production architecture used in industry applications.

---

## Current Features

### Pantry Management
- Add, edit, and delete pantry items  
- Clean React state management (immutability, lifted state)  
- Full CRUD integration with backend  
- Persistent storage using SQLite (via SQLAlchemy ORM)  


### Backend (FastAPI + SQLAlchemy)
- REST API with proper HTTP semantics  
- SQLite persistence via SQLAlchemy ORM  
- Clear separation between:
  - API routes  
  - CRUD logic  
  - Database models  
- Meaningful errors (400, 404, 204)  
- CORS-enabled for frontend communication 

### Frontend
- React Router multi-page layout  
- Centralized Axios API client  
- Automatic data refresh after writes  

---

## Database Architecture

Pantry Planner now uses a real database layer:

- **SQLite** — fast and lightweight for local development  
- **SQLAlchemy** — models + queries, not raw SQL  

Current tables include:

- pantry items
- (in progress) canonical ingredients + recipes
- (planned) recipe–ingredient relationships

This foundation enables smarter features like recipe suggestions and shopping lists.

---

## Project Structure
```
pantry-planner/
├── frontend/
│   └── src/
│       ├── api/
│       │   └── client.js
│       ├── pages/
│       │   ├── Home.js
│       │   ├── Pantry.js
│       │   ├── Recipes.js
│       │   └── ShoppingList.js
│       ├── IngredientList.js
│       ├── App.js
│       └── index.js
│
├── backend/
│   ├── main.py          # FastAPI app + routes
│   ├── crud.py          # Database operations
│   ├── models.py        # SQLAlchemy models
│   ├── database.py      # Engine + session management
│   ├── init_db.py       # DB initialization script
│   └── pantry.db        # (ignored in git)
│
└── README.md
```

---

## What I’ve Learned So Far

- Designing a backend as the **authoritative data source**
- Implementing CRUD APIs correctly
- Using SQLAlchemy instead of in-memory storage
- Separating:
  - routes  
  - business logic  
  - database models  
- Debugging using Swagger + DevTools  
- Maintaining a clean Git history  

---

## Planned Enhancements

- Ingredient + Recipe data model (many-to-many)
- Recipe suggestions based on pantry contents
- Shopping list generation
- Per-user pantries
- Deployment (Render / Railway / Vercel)
- Database migrations as schema evolves


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

## Notes

- `pantry.db` is **not tracked in Git** (on purpose)  
  Databases are environment-specific and can be regenerated.  

---

## Contact

**Miguel Salvador**  
Computer Science Student | Portland State University

- GitHub: [https://github.com/msalvad2](https://github.com/msalvad2)
- LinkedIn: [https://www.linkedin.com/in/miguel-salvador-4049a528b/](https://www.linkedin.com/in/miguel-salvador-4049a528b/)
