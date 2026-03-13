import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import App from '../src/App';

describe('App component', () => {
  it('renders without crashing', () => {
    render(<App />);
    expect(screen.getByText(/ToDo List/i)).toBeInTheDocument();
  });
});