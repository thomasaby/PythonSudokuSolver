
# 🧩 Sudoku Solver Web App

A simple web-based Sudoku Solver built with Python (Flask) and HTML/CSS/JavaScript.

---

## 🚀 Features

- Solve any valid 9x9 Sudoku puzzle
- Interactive grid-based input
- Backend solver using backtracking algorithm
- Object-oriented design using a `SudokuSolver` class
- Clean and responsive UI

---

## 🗂️ Project Structure

```
sudoku-solver/
├── backend/
│   ├── app.py           # Flask app
│   ├── solver.py        # SudokuSolver class
│   └── static/
│       ├── index.html   # Frontend UI
│       ├── style.css    # Styling
│       └── script.js    # Grid + solve logic
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/thomasaby/PythonSudokuSolver.git
cd sudoku-solver/backend
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser 🎉

---

## 💡 How It Works

- The user inputs a Sudoku board in the browser.
- On clicking **Solve**, the board is sent to the backend via a POST request.
- The `SudokuSolver` class uses a backtracking algorithm to solve the puzzle.
- The solution is returned to the frontend and displayed in the grid.

---

## 📦 Dependencies

- Python 3.x
- Flask

---

## ✨ Future Ideas

- Add visual step-by-step solving
- Add "Clear" and "Validate" buttons
- Mobile-friendly UI

---

## 📄 License

MIT License
