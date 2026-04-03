<script setup>
import { ref, onMounted } from 'vue'

// Reactive state
const tasks = ref([])
const newTaskTitle = ref('')
const loading = ref(false)

// 1. GET: Fetch all tasks from FastAPI
const fetchTasks = async () => {
  loading.value = true
  try {
    const response = await fetch('http://localhost:8000/tasks')
    tasks.value = await response.json()
  } catch (error) {
    console.error("Failed to fetch tasks:", error)
  } finally {
    loading.value = false
  }
}

// 2. POST: Add a new task to PostgreSQL
const addTask = async () => {
  if (!newTaskTitle.value.trim()) return
  
  try {
    // Sending title as a query parameter (matches your FastAPI POST route)
    await fetch(`http://localhost:8000/tasks?title=${encodeURIComponent(newTaskTitle.value)}`, { 
      method: 'POST' 
    })
    newTaskTitle.value = '' // Clear input
    fetchTasks()            // Refresh list
  } catch (error) {
    console.error("Error adding task:", error)
  }
}

// 3. DELETE: Remove a task
const deleteTask = async (id) => {
  try {
    await fetch(`http://localhost:8000/tasks/${id}`, { method: 'DELETE' })
    fetchTasks()
  } catch (error) {
    console.error("Error deleting task:", error)
  }
}

onMounted(fetchTasks)
</script>

<template>
  <div class="app-container">
    <header>
      <h1>Full Stack Todo List</h1>
      <p>FastAPI + PostgreSQL + Vue 3</p>
    </header>

    <main>
      <div class="input-section">
        <input 
          v-model="newTaskTitle" 
          placeholder="Enter a new task..." 
          @keyup.enter="addTask"
        />
        <button @click="addTask" :disabled="!newTaskTitle">Add</button>
      </div>

      <div v-if="loading" class="status">Loading tasks...</div>

      <ul v-else class="task-list">
        <li v-for="task in tasks" :key="task.id" class="task-card">
          <span>{{ task.title }}</span>
          <button @click="deleteTask(task.id)" class="delete-btn">Delete</button>
        </li>
      </ul>

      <div v-if="!loading && tasks.length === 0" class="status">
        No tasks found. Add one above!
      </div>
    </main>
  </div>
</template>

<style>
/* Simple Global CSS */
body {
  background-color: #121212;
  color: #e0e0e0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  display: flex;
  justify-content: center;
}

.app-container {
  width: 100%;
  max-width: 500px;
  padding: 40px 20px;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

header h1 { color: #42b883; margin-bottom: 5px; font-size:2rem}
header p { color: #888; font-size: 0.9rem; }

.input-section {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
}

input {
  flex: 1;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid #333;
  background: #1e1e1e;
  color: white;
  outline: none;
}

input:focus { border-color: #42b883; }

button {
  padding: 10px 20px;
  background-color: #42b883;
  border: none;
  border-radius: 6px;
  color: #121212;
  font-weight: bold;
  cursor: pointer;
}

button:disabled { opacity: 0.5; cursor: not-allowed; }

.task-list {
  list-style: none;
  padding: 0;
}

.task-card {
  background: #1e1e1e;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-left: 4px solid #42b883;
}

.delete-btn {
  background-color: #ff5252;
  color: white;
  padding: 5px 10px;
  font-size: 0.8rem;
}

.status { text-align: center; color: #666; margin-top: 20px; }
</style>