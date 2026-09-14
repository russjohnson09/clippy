const http = require('http');
const { server, handleRequest, TODOS } = require('./server');

const BASE_URL = 'http://localhost:3000';

function request(method, path, data = null) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'localhost',
      port: 3000,
      path,
      method,
    };

    const req = http.request(options, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, body: body ? JSON.parse(body) : null });
        } catch {
          resolve({ status: res.statusCode, body });
        }
      });
    });

    req.on('error', reject);
    if (data) req.write(JSON.stringify(data));
    req.end();
  });
}

beforeAll(async () => {
  await new Promise(resolve => setTimeout(resolve, 100));
});

afterAll(async () => {
  TODOS.clear();
  server.close();
});

describe('GET /todos', () => {
  it('should return empty array when no todos exist', async () => {
    const result = await request('GET', '/todos');
    expect(result.status).toBe(200);
    expect(result.body).toEqual([]);
  });

  it('should return all todos', async () => {
    TODOS.set('1', { text: 'Buy milk', completed: false });
    TODOS.set('2', { text: 'Walk dog', completed: true });

    const result = await request('GET', '/todos');
    expect(result.status).toBe(200);
    expect(result.body).toHaveLength(2);
  });
});

describe('GET /todos/:id', () => {
  it('should return a specific todo', async () => {
    TODOS.set('123', { text: 'Test todo', completed: false });

    const result = await request('GET', '/todos/123');
    expect(result.status).toBe(200);
    expect(result.body).toEqual({ id: '123', text: 'Test todo', completed: false });
  });

  it('should return 404 for non-existent todo', async () => {
    const result = await request('GET', '/todos/999');
    expect(result.status).toBe(404);
  });
});

describe('POST /todos', () => {
  it('should create a new todo', async () => {
    const newTodo = { text: 'New task' };
    const result = await request('POST', '/todos', newTodo);

    expect(result.status).toBe(201);
    expect(result.body).toHaveProperty('id');
    expect(result.body.id).not.toBeUndefined();
    expect(result.body.text).toBe('New task');
    expect(result.body.completed).toBe(false);
  });

  it('should create todo with empty text', async () => {
    const result = await request('POST', '/todos', {});
    expect(result.status).toBe(201);
    expect(result.body).toHaveProperty('id');
  });
});

describe('PUT /todos/:id', () => {
  it('should update a todo', async () => {
    TODOS.set('1', { text: 'Original', completed: false });

    const update = { text: 'Updated', completed: true };
    const result = await request('PUT', '/todos/1', update);

    expect(result.status).toBe(200);
    expect(result.body.text).toBe('Updated');
    expect(result.body.completed).toBe(true);
  });

  it('should return 404 for non-existent todo', async () => {
    const update = { text: 'Update' };
    const result = await request('PUT', '/todos/999', update);
    expect(result.status).toBe(404);
  });
});

describe('DELETE /todos/:id', () => {
  it('should delete a todo', async () => {
    TODOS.set('1', { text: 'To delete', completed: false });

    const result = await request('DELETE', '/todos/1');
    expect(result.status).toBe(204);

    const listResult = await request('GET', '/todos');
    expect(listResult.body).toHaveLength(0);
  });

  it('should return 404 for non-existent todo', async () => {
    const result = await request('DELETE', '/todos/999');
    expect(result.status).toBe(404);
  });
});

describe('Error handling', () => {
  it('should return 405 for unsupported methods', async () => {
    const result = await request('PATCH', '/todos/1');
    expect(result.status).toBe(405);
  });
});
