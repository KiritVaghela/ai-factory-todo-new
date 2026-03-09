import React from 'react';

function DeleteButton({ taskId, onDelete }) {
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      onDelete(taskId);
    }
  };

  return <button onClick={handleDelete}>Delete</button>;
}

export default DeleteButton;