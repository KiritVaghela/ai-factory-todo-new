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
    <div>
      <h1>ToDo App</h1>
      <form onSubmit={submitTask}>
        <input
          type="text"
          value={taskTitle}
          onChange={(e) => setTaskTitle(e.target.value)}
          placeholder="Add a new task"
          required
        />
        <button type="submit">Submit</button>
      </form>
      <div id="tasks-container">
        {tasks.map((task) => (
          <div key={task.id} className="task">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => toggleTaskCompletion(task)}
            />
            <span>{task.title}</span>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
