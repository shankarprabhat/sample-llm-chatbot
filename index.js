const express = require("express");
const axios = require("axios");
const app = express();
const cors = require('cors');

app.use(express.static('public')); // For serving HTML/CSS
app.use(express.json());
app.use(cors());

app.post("/send-message", async (req, res) => {
    const message = req.body.message;

    try {
        const response = await axios.post('http://<flask_server_url>/chat', {
            message: message
        });
        res.json(response.data);
    } catch (error) {
        res.status(500).send("Error communicating with Python API");
    }
});

// Use the environment variable
const port = process.env.PORT || 3000; // Default to 3000 if PORT is not set

// If using local, Start the server
// app.listen(port, () => {
//     console.log("Server running on http://localhost:3000");
// });

// Export the app for Vercel
module.exports = app;

// app.listen(3000, () => {
//     console.log("Node.js server running on port 3000");
// });
