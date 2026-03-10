import React from 'react';
import PropTypes from 'prop-types';

/**
 * DeleteButton component renders a button for deleting a task.
 * @param {Object} props
 * @param {function} props.onClick - Function to call when button is clicked
 * @param {string} [props.className] - Additional class names for styling
 * @returns {JSX.Element}
 */
const DeleteButton = ({ onClick, className = '' }) => {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`text-red-500 hover:text-red-700 focus:outline-none ${className}`}
      aria-label="Delete task"
    >
      {/* FontAwesome trash icon, fallback to 'X' if icon not available */}
      <i className="fas fa-trash-alt" aria-hidden="true"></i>
      <span className="sr-only">Delete</span>
    </button>
  );
};

DeleteButton.propTypes = {
  onClick: PropTypes.func.isRequired,
  className: PropTypes.string,
};

export default DeleteButton;
