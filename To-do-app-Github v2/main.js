// Get DOM elements
const submitButton = document.getElementById("submit");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

// Add task functionality
submitButton.addEventListener("click", function (e) {
  e.preventDefault();
  const task = taskInput.value.trim();
  if (!task) return;

  addTask(task);
  taskInput.value = "";
});

// Enter key to add task
taskInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    e.preventDefault();
    const task = taskInput.value.trim();
    if (!task) return;

    addTask(task);
    taskInput.value = "";
  }
});

// Function to add a new task
function addTask(taskText) {
  const li = document.createElement("li");
  li.innerHTML = `
    <span class="task-text">${taskText}</span>
    <div class="action-btns">
      <button class="view-btn">View</button>
      <button class="edit-btn">Edit</button>
      <button class="remove-btn">Delete</button>
    </div>
  `;
  taskList.appendChild(li);
}

// Event delegation for all buttons
taskList.addEventListener("click", function (e) {
  const target = e.target;
  const li = target.closest("li");
  
  if (!li) return;

  // Delete functionality
  if (target.classList.contains("remove-btn")) {
    li.remove();
  }
  
  // Edit functionality
  else if (target.classList.contains("edit-btn")) {
    const taskText = li.querySelector(".task-text");
    const updated = prompt("Edit task:", taskText.textContent);
    if (updated && updated.trim()) {
      taskText.textContent = updated.trim();
    }
  }
  
  // View functionality
  else if (target.classList.contains("view-btn")) {
    const taskText = li.querySelector(".task-text");
    alert(`Task: ${taskText.textContent}`);
  }
});

// Add event listeners to existing static tasks
document.addEventListener("DOMContentLoaded", function() {
  // The existing static tasks will now work with the event delegation above
  console.log("Todo app loaded successfully!");
});