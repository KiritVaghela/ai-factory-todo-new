import React from 'react';
import './TaskList.css';

function TaskList({ tasks, onDelete }) {
  return (
    <div className="task-list">
      {tasks.map((task) => (
        <div key={task.id} className="task-item">
          <span>{task.title}</span>
          <button onClick={() => onDelete(task.id)} className="delete-button">
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

export default TaskList;
