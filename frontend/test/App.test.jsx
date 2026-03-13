import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import App from '../src/App.jsx';

vi.mock('axios');

describe('App', () => {
  it('renders the todo list title', () => {
    render(<App />);
    expect(screen.getByText('ToDo List')).toBeInTheDocument();
  });

  it('allows adding a new task', async () => {
    render(<App />);
    const input = screen.getByRole('textbox');
    const addButton = screen.getByRole('button', { name: /add/i });

    fireEvent.change(input, { target: { value: 'New Task' } });
    fireEvent.click(addButton);

    expect(await screen.findByText('New Task')).toBeInTheDocument();
  });
});