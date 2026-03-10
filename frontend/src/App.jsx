import React, { useState, useEffect } from 'react';
import axios from 'axios';
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

  return (
    <div className="max-w-xl mx-auto p-4 bg-white rounded shadow">
      <form onSubmit={submitTask} className="flex mb-4">
        <input
          type="text"
          className="flex-1 border rounded-l px-3 py-2 focus:outline-none"
          placeholder="Add a new task..."
          value={taskTitle}
          onChange={e => setTaskTitle(e.target.value)}
          required
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600"
        >
          Add
        </button>
      </form>
      <ul className="divide-y">
        {tasks.map(task => (
          <li key={task.id} className="flex items-center py-2">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => toggleTaskCompletion(task)}
              className="mr-2"
            />
            <span className={task.completed ? 'line-through flex-1' : 'flex-1'}>{task.title}</span>
            <button
              onClick={() => deleteTask(task.id)}
              className="ml-2 text-red-500 hover:text-red-700"
              aria-label="Delete task"
            >
              &#10005;
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
