import React from 'react';
import PropTypes from 'prop-types';
import './DeleteButton.css';

function DeleteButton({ onClick }) {
  return (
    <button className="delete-button" onClick={onClick} style={{ margin: '10px' }}>
      Delete
    </button>
  );
}

DeleteButton.propTypes = {
  onClick: PropTypes.func.isRequired,
};

export default DeleteButton;
