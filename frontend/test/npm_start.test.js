import { render, screen } from '@testing-library/react';
import App from '../src/App';

// Mock axios
jest.mock('axios');

describe('App component', () => {
  test('renders ToDo List heading', () => {
    render(<App />);
    const headingElement = screen.getByText(/ToDo List/i);
    expect(headingElement).toBeInTheDocument();
  });
});