import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles.css';

function App() {
  // State to hold task input
  const [taskTitle, setTaskTitle] = useState('');
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch tasks from server on component mount
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://localhost:8000/tasks/');
        setTasks(response.data);
        setError(null);
      } catch (error) {
        setError('Error fetching tasks');
      } finally {
        setLoading(false);
      }
    };
    fetchTasks();
  }, []);

  // Function to handle task submission
  const submitTask = async (event) => {
    event.preventDefault();
    if (!taskTitle.trim()) return;
    try {
      const response = await axios.post('http://localhost:8000/tasks/', {
        title: taskTitle,
        completed: false
      });
      setTasks([...tasks, response.data]);
      setTaskTitle('');
      setError(null);
    } catch (error) {
      setError('Error submitting task');
    }
  };

  // Function to handle task completion state change
  const toggleTaskCompletion = async (task) => {
    try {
      const updatedTask = { ...task, completed: !task.completed };
      await axios.put(`http://localhost:8000/tasks/${task.id}`, updatedTask);
      setTasks(tasks.map(t => (t.id === task.id ? updatedTask : t)));
      setError(null);
    } catch (error) {
      setError('Error updating task');
    }
  };

  // Function to handle task deletion
  const deleteTask = async (taskId) => {
    try {
      await axios.delete(`http://localhost:8000/tasks/${taskId}`);
      setTasks(tasks.filter(task => task.id !== taskId));
      setError(null);
    } catch (error) {
      setError('Error deleting task');
    }
  };

  return (
    <div className="max-w-xl mx-auto bg-white rounded shadow p-6">
      <form onSubmit={submitTask} className="flex mb-6">
        <input
          type="text"
          className="flex-1 border border-gray-300 rounded-l px-3 py-2 focus:outline-none"
          placeholder="Add a new task..."
          value={taskTitle}
          onChange={e => setTaskTitle(e.target.value)}
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600"
        >
          Add
        </button>
      </form>
      {error && <div className="text-red-500 mb-2">{error}</div>}
      {loading ? (
        <div className="text-gray-500">Loading tasks...</div>
      ) : (
        <ul className="divide-y divide-gray-200">
          {tasks.length === 0 ? (
            <li className="text-gray-400">No tasks yet.</li>
          ) : (
            tasks.map(task => (
              <li key={task.id} className="flex items-center py-2">
                <input
                  type="checkbox"
                  checked={!!task.completed}
                  onChange={() => toggleTaskCompletion(task)}
                  className="mr-3"
                />
                <span className={task.completed ? 'line-through text-gray-400 flex-1' : 'flex-1'}>
                  {task.title}
                </span>
                <button
                  onClick={() => deleteTask(task.id)}
                  className="ml-3 text-red-500 hover:text-red-700"
                  title="Delete"
                >
                  <i className="fas fa-trash"></i>
                </button>
              </li>
            ))
          )}
        </ul>
      )}
    </div>
  );
}

export default App;
