import { expect, test } from '@jest/globals';
import { setupServer } from 'msw/node';
import { rest } from 'msw';

// Initialize server
const server = setupServer(
  rest.post('http://localhost:8000/tasks/', (req, res, ctx) => {
    return res(ctx.json({ id: 1, title: req.body.title, completed: req.body.completed }));
  }),
  rest.get('http://localhost:8000/tasks/', (req, res, ctx) => {
    return res(ctx.json([{ id: 1, title: 'Sample Task', completed: false }]));
  }),
  rest.put('http://localhost:8000/tasks/:taskId', (req, res, ctx) => {
    const { taskId } = req.params;
    return res(ctx.json({ id: taskId, title: req.body.title, completed: req.body.completed }));
  }),
  rest.delete('http://localhost:8000/tasks/:taskId', (req, res, ctx) => {
    return res(ctx.json({ message: 'Task deleted successfully' }));
  })
);

// Establish API mocking before all tests.
beforeAll(() => server.listen());

// Clean up after the tests are finished.
afterEach(() => server.resetHandlers());

// Clean up after the server is stopped.
afterAll(() => server.close());

// Test cases to verify API behavior

test('Can create task', async () => {
    const response = await fetch('http://localhost:8000/tasks/', {
      method: 'POST',
      body: JSON.stringify({ title: 'Test Task', completed: false }),
      headers: { 'Content-Type': 'application/json' },
    });
    const data = await response.json();
    expect(response.status).toBe(200);
    expect(data.title).toBe('Test Task');
});


test('Can get tasks', async () => {
    const response = await fetch('http://localhost:8000/tasks/');
    const data = await response.json();
    expect(response.status).toBe(200);
    expect(data).toBeInstanceOf(Array);
});


test('Can update task', async () => {
    const response = await fetch('http://localhost:8000/tasks/1', {
      method: 'PUT',
      body: JSON.stringify({ title: 'Updated Task', completed: true }),
      headers: { 'Content-Type': 'application/json' },
    });
    const data = await response.json();
    expect(response.status).toBe(200);
    expect(data.title).toBe('Updated Task');
    expect(data.completed).toBe(true);
});


test('Can delete task', async () => {
    const response = await fetch('http://localhost:8000/tasks/1', {
      method: 'DELETE',
    });
    const data = await response.json();
    expect(response.status).toBe(200);
    expect(data.message).toBe('Task deleted successfully');
});
