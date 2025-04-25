from flask import Flask, request, jsonify, send_from_directory
from solver import SudokuSolver
import os

# Set up Flask app
app = Flask(__name__, static_folder='static')

# Serve the main HTML page
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve other static files (CSS, JS)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# Handle the solving logic
@app.route('/solve', methods=['POST'])
def solve_sudoku():
    data = request.get_json()
    board = data.get('board')

    if not board or len(board) != 9 or any(len(row) != 9 for row in board):
        return jsonify({"error": "Invalid board"}), 400

    solver = SudokuSolver(board)
    solution = solver.get_solution()

    if solution:
        return jsonify({"solution": solution})
    else:
        return jsonify({"error": "No solution found"}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
