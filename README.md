# Pantry Planner 🥗

🚧 **Work in Progress** 🚧

Pantry Planner is a full-stack web application designed to help students and busy users plan meals based on the ingredients they already have. The goal is to reduce food waste, save money, and make cooking decisions easier.

---

## Motivation

As a student, I often had ingredients available but no clear idea what meals I could actually make with them. Pantry Planner helps answer questions like:

- *What can I cook with what I already have?*
- *What ingredients am I missing for a recipe?*
- *What should I buy next time I go shopping?*

This project also serves as a hands-on learning experience for building a **real-world full-stack application** with clean separation of concerns between frontend and backend.

---

## Tech Stack

### Frontend
- **React** with Hooks (`useState`, `useEffect`)
- **React Router** for multi-page navigation
- **Fetch API** for HTTP requests
- HTML / CSS / JavaScript

### Backend
- **Python**
- **FastAPI** framework
- RESTful API design
- CORS configuration for cross-origin requests

---

## Architecture Overview

This project follows modern full-stack patterns:

- The **backend serves as the single source of truth** for all data
- The **frontend fetches and syncs** data through REST API calls
- All CRUD operations (`Create`, `Read`, `Update`, `Delete`) are performed via API endpoints
- React manages UI state while staying synchronized with backend state

This architecture mirrors real production application design.

---

## Current Features

✅ **Pantry Management**
- Add new ingredients
- Edit existing ingredients
- Delete ingredients

✅ **Backend**
- RESTful API endpoints (`GET`, `POST`)
- `PUT` and `DELETE` endpoints in progress
- In-memory data persistence
- CORS-enabled for frontend communication

✅ **Frontend**
- Clean React state management with immutability
- Multi-page navigation using React Router
- Real-time UI updates synced with backend

---

## Planned Features

🔜 Upcoming improvements:

- Recipe matching algorithm based on available ingredients
- Shopping list generation for missing ingredients
- Database integration (SQLite or PostgreSQL)
- Enhanced UI/UX with modern styling
- Comprehensive error handling and loading states
- Production deployment

---

## How to Run Locally

### Prerequisites
- Python 3.8+
- Node.js and npm

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will run at: `http://localhost:8000`  
Swagger UI documentation: `http://localhost:8000/docs`

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

The app will run at: `http://localhost:3000`

---

## Project Structure
```
pantry-planner/
├── backend/
│   ├── main.py              # FastAPI application
│ 
├── frontend/
│   ├── src/
│   │   ├── pages/          # React components
│   │   └── App.js          # Main app component
│   └── package.json        # Node dependencies
└── README.md
```

---

## Learning Goals

This project demonstrates:
- Full-stack development with React and FastAPI
- RESTful API design and implementation
- State management and data synchronization
- Frontend-backend communication patterns
- Clean code organization and separation of concerns

---

## Project Status

This project is **actively being developed**. Features, structure, and documentation will continue to evolve as new functionality is added.

---

## Contact

**Miguel Salvador**  
Computer Science Student | Portland State University  
[GitHub Profile](https://github.com/msalvad2) | [LinkedIn](https://www.linkedin.com/in/miguel-salvador-4049a528b/)
