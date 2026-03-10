import React from 'react';
import PropTypes from 'prop-types';

/**
 * TaskList component displays a list of tasks with completion and delete options.
 * @param {Object[]} tasks - Array of task objects.
 * @param {Function} onToggleComplete - Function to toggle completion status.
 * @param {Function} onDelete - Function to delete a task.
 */
function TaskList({ tasks, onToggleComplete, onDelete }) {
  return (
    <ul className="list-group mt-4">
      {tasks && tasks.length > 0 ? (
        tasks.map((task) => (
          <li
            key={task.id}
            className={`list-group-item d-flex justify-content-between align-items-center ${task.completed ? 'bg-success text-white' : ''}`}
          >
            <span
              style={{
                textDecoration: task.completed ? 'line-through' : 'none',
                cursor: 'pointer',
              }}
              onClick={() => onToggleComplete(task)}
              title="Toggle complete"
            >
              {task.title}
            </span>
            <div>
              <button
                className={`btn btn-sm ${task.completed ? 'btn-secondary' : 'btn-outline-success'} mr-2`}
                onClick={() => onToggleComplete(task)}
                aria-label={task.completed ? 'Mark as incomplete' : 'Mark as complete'}
              >
                {task.completed ? (
                  <i className="fas fa-undo"></i>
                ) : (
                  <i className="fas fa-check"></i>
                )}
              </button>
              <button
                className="btn btn-sm btn-danger"
                onClick={() => onDelete(task.id)}
                aria-label="Delete task"
              >
                <i className="fas fa-trash"></i>
              </button>
            </div>
          </li>
        ))
      ) : (
        <li className="list-group-item text-center text-muted">No tasks found.</li>
      )}
    </ul>
  );
}

TaskList.propTypes = {
  tasks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      completed: PropTypes.bool.isRequired,
    })
  ).isRequired,
  onToggleComplete: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

export default TaskList;
