function createBoard() {
    const table = document.getElementById("sudoku-board");
    for (let row = 0; row < 9; row++) {
      const tr = document.createElement("tr");
      for (let col = 0; col < 9; col++) {
        const td = document.createElement("td");
        const input = document.createElement("input");
        input.type = "number";
        input.min = 1;
        input.max = 9;
        input.classList.add("cell");
        td.appendChild(input);
        tr.appendChild(td);
      }
      table.appendChild(tr);
    }
  }
  
  async function submitBoard() {
    const board = [];
    document.querySelectorAll("tr").forEach(row => {
      const nums = [];
      row.querySelectorAll("input").forEach(cell => {
        const val = parseInt(cell.value);
        nums.push(isNaN(val) ? 0 : val);
      });
      board.push(nums);
    });
  
    const response = await fetch("/solve", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ board }),
    });
  
    const data = await response.json();
    if (data.solution) {
      updateBoard(data.solution);
    } else {
      alert(data.error || "Unable to solve puzzle.");
    }
  }
  
  function updateBoard(solution) {
    const cells = document.querySelectorAll("input");
    let index = 0;
    for (let row of solution) {
      for (let num of row) {
        cells[index].value = num;
        index++;
      }
    }
  }
  
  createBoard();
  