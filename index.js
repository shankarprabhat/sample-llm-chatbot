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

app.listen(3000, () => {
    console.log("Node.js server running on port 3000");
});
