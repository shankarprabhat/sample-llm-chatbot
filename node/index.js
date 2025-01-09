const express = require("express");
const app = express();
const cors = require('cors');

app.use(express.static('public')); // For serving HTML/CSS
app.use(express.json());
app.use(cors());

const port = process.env.PORT || 3000; // Default to 3000 if PORT is not set

// Export the app for Vercel
module.exports = app;
