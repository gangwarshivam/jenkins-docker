const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const path = require('path');

// express → Imports Express framework to create the frontend server.
// body-parser → Middleware to read form data from requests.
// axios → Used to send HTTP POST request from frontend to backend.
// path → Helps access and work with file system paths (used for sending HTML file).


const app = express(); //this app represent a frontend webserver
const PORT = process.env.PORT || 3000;

// below two middlewares allows server to read incoming data. Without these express cannot read form fields sent by the users
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Serve static (if any)
app.use('/static', express.static(path.join(__dirname, 'public')));

// Serve the HTML form when a user visit localhost:3000
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'form.html'));
});

// Handle form submission from browser, forwards data as JSON to backend service url to Flask backend
app.post('/submit', async (req, res) => {
  try {
    // Compose payload to send to backend
    const payload = {
      name: req.body.name,
      email: req.body.email,
      message: req.body.message
    };

    // Backend service name is "backend" in docker-compose; port 5000
    // Allows backend URL to be configurable using environment variable BACKEND_URL.
    // If not provided, it defaults to:
    const backendUrl = process.env.BACKEND_URL || 'http://backend:5000/process';

    // Forward the request (as JSON). Sends the form data to the Flask backend using Axios.
    const response = await axios.post(backendUrl, payload, {
      headers: { 'Content-Type': 'application/json' },
      timeout: 5000
    });

    // Send a friendly success page or redirect
    res.send(`<h2>Backend response</h2><pre>${JSON.stringify(response.data, null, 2)}</pre><p><a href="/">Back</a></p>`);
  } catch (err) {
    console.error('Error forwarding to backend:', err.message || err);
    const message = err.response ? JSON.stringify(err.response.data) : err.message;
    res.status(500).send(`<h2>Error</h2><pre>${message}</pre><p><a href="/">Back</a></p>`);
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});
