import React from 'react';

const DeleteButton = ({ onClick }) => {
  return (
    <button className="new-css-class" onClick={onClick}> {/* Use the new CSS class */}
      Delete
    </button>
  );
};

export default DeleteButton;
