import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { createRoot } from 'react-dom/client';
import './styles.css'; // Import Tailwind CSS here

function App() {
  console.log('Rendering App component');

  // State to hold task input
  const [taskTitle, setTaskTitle] = useState('');
  const [tasks, setTasks] = useState([]);

  // Fetch tasks from server on component mount
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const response = await axios.get('http://localhost:8000/tasks/');
        setTasks(response.data);
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    };
    fetchTasks();
  }, []);

  // Function to handle task submission
  const submitTask = async (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
    try {
      const response = await axios.post('http://localhost:8000/tasks/', {
        title: taskTitle,
        completed: false
      });
      setTasks([...tasks, response.data]); // Update tasks with the new task
      setTaskTitle(''); // Clear the input field
    } catch (error) {
      console.error('Error submitting task:', error);
    }
  };

  // Function to handle task completion state change
  const toggleTaskCompletion = async (task) => {
    try {
      const updatedTask = { ...task, completed: !task.completed };
      await axios.put(`http://localhost:8000/tasks/${task.id}`, updatedTask);
      setTasks(tasks.map(t => (t.id === task.id ? updatedTask : t))); // Update tasks with the modified task
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  // Function to handle task deletion
  const deleteTask = async (taskId) => {
    try {
      await axios.delete(`http://localhost:8000/tasks/${taskId}`);
      setTasks(tasks.filter(task => task.id !== taskId)); // Remove the deleted task from state
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  // UI Tests for Desktop and Mobile

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">ToDo App</h1>
      <form onSubmit={submitTask} className="mb-4">
        <input
          type="text"
          value={taskTitle}
          onChange={(e) => setTaskTitle(e.target.value)}
          className="border rounded p-2"
          placeholder="Add a new task..."
          required
        />
        <button type="submit" className="ml-2 bg-blue-500 text-white rounded p-2">Add Task</button>
      </form>
      <ul>
        {tasks.map(task => (
          <li key={task.id} className="flex justify-between items-center">
            <span className={task.completed ? 'line-through' : ''}>{task.title}</span>
            <div>
              <button onClick={() => toggleTaskCompletion(task)} className="bg-yellow-500 text-white rounded p-1 mr-2">Toggle</button>
              <button onClick={() => deleteTask(task.id)} className="bg-red-500 text-white rounded p-1">Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
