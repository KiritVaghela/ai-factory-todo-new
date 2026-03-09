import React from 'react';
import './DeleteButton.css'; // Assuming the new CSS class is defined here

const DeleteButton = ({ onClick }) => {
  return (
    <button className="new-css-class" onClick={onClick}> {/* Use the new CSS class */}
      Delete
    </button>
  );
};

export default DeleteButton;
