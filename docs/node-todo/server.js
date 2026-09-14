const http = require('http');

const TODOS = new Map();

function parseBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try {
        resolve(body ? JSON.parse(body) : {});
      } catch (e) {
        reject(e);
      }
    });
    req.on('error', reject);
  });
}

async function handleRequest(req, res) {
  const { method, url } = req;
  const pathname = url.split('?')[0];
  const parts = pathname.split('/').filter(Boolean);

  res.setHeader('Content-Type', 'application/json');

  try {
    switch (method) {
      case 'GET': {
        if (pathname === '/todos') {
          const todos = [];
          for (const [id, todo] of TODOS.entries()) {
            todos.push({ id, text: todo.text, completed: todo.completed });
          }
          res.statusCode = 200;
          res.end(JSON.stringify(todos));
        } else if (parts.length >= 2 && parts[parts.length - 1]) {
          const id = parts[parts.length - 1];
          const todo = TODOS.get(id);
          if (!todo) {
            res.statusCode = 404;
            res.end(JSON.stringify({ error: 'Todo not found' }));
            return;
          }
          res.statusCode = 200;
          res.end(JSON.stringify({ id, text: todo.text, completed: todo.completed }));
        } else {
          res.statusCode = 404;
          res.end(JSON.stringify({ error: 'Not found' }));
        }
        break;
      }

      case 'POST': {
        if (pathname === '/todos') {
          const body = await parseBody(req);
          const id = String(TODOS.size + 1);
          TODOS.set(id, { text: body.text || '', completed: false });
          res.statusCode = 201;
          res.end(JSON.stringify({ id, text: body.text || '', completed: false }));
        } else {
          res.statusCode = 404;
          res.end(JSON.stringify({ error: 'Not found' }));
        }
        break;
      }

      case 'PUT': {
        if (parts.length >= 2 && parts[parts.length - 1]) {
          const id = parts[parts.length - 1];
          const todo = TODOS.get(id);
          if (!todo) {
            res.statusCode = 404;
            res.end(JSON.stringify({ error: 'Todo not found' }));
            return;
          }
          const body = await parseBody(req);
          todo.text = body.text !== undefined ? body.text : todo.text;
          todo.completed = body.completed !== undefined ? body.completed : todo.completed;
          res.statusCode = 200;
          res.end(JSON.stringify({ id, text: todo.text, completed: todo.completed }));
        } else {
          res.statusCode = 400;
          res.end(JSON.stringify({ error: 'Missing todo id' }));
        }
        break;
      }

      case 'DELETE': {
        if (parts.length >= 2 && parts[parts.length - 1]) {
          const id = parts[parts.length - 1];
          if (!TODOS.has(id)) {
            res.statusCode = 404;
            res.end(JSON.stringify({ error: 'Todo not found' }));
            return;
          }
          TODOS.delete(id);
          res.statusCode = 204;
          res.end();
        } else {
          res.statusCode = 400;
          res.end(JSON.stringify({ error: 'Missing todo id' }));
        }
        break;
      }

      default:
        res.statusCode = 405;
        res.end(JSON.stringify({ error: 'Method not allowed' }));
    }
  } catch (err) {
    console.error(err);
    res.statusCode = 500;
    res.end(JSON.stringify({ error: 'Internal server error' }));
  }
}

const server = http.createServer(handleRequest);

module.exports = { server, handleRequest, TODOS };
