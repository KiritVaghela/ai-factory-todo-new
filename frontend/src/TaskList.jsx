import React from 'react';
import axios from 'axios';

function TaskList() {
  const [tasks, setTasks] = React.useState([]);

  React.useEffect(() => {
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

  const handleCheckboxChange = async (taskId, checked) => {
    // Handle checkbox change logic here if needed
  };

  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id} style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
          <input
            type="checkbox"
            checked={task.completed}
            onChange={(e) => handleCheckboxChange(task.id, e.target.checked)}
            disabled={task.completed} // Disable checkbox if task is completed
          />
          {task.title}
        </li>
      ))}
    </ul>
  );
}

export default TaskList;
