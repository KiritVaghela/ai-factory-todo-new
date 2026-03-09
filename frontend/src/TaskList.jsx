import React, { useState } from 'react';
import axios from 'axios';

// Checkbox component
const Checkbox = ({ checked, onChange }) => {
  return (
    <input type='checkbox' checked={checked} onChange={onChange} />
  );
};

function TaskList() {
  const [taskTitle, setTaskTitle] = useState('');
  const [tasks, setTasks] = useState([]);

  const submitTask = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/tasks/', {
        title: taskTitle,
        completed: false
      });
      setTasks([...tasks, response.data]);
      setTaskTitle('');
    } catch (error) {
      console.error('Error submitting task:', error);
    }
  };

  const toggleTaskCompletion = async (task) => {
    try {
      const updatedTask = { ...task, completed: !task.completed };
      await axios.put(`http://localhost:8000/tasks/${task.id}`, updatedTask);
      setTasks(tasks.map(t => (t.id === task.id ? updatedTask : t)));
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
            <Checkbox
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

export default TaskList;
