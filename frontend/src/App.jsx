import React, { useState, useEffect } from 'react';
import axios from 'axios';

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

  return (
    <div>
      <h1>Simple ToDo App</h1>
      <form onSubmit={submitTask}>
        <input
          type="text"
          value={taskTitle}
          onChange={(e) => setTaskTitle(e.target.value)}
          placeholder="Enter a new task"
        />
        <button type="submit">Add Task</button>
      </form>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => toggleTaskCompletion(task)}
            />
            {task.title}
          </li>
        ))}
      </ul>
      <p>Manage your tasks efficiently!</p>
    </div>
  );
}

export default App;