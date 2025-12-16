// app.js - Simple Express.js REST API
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Simple calculator functions
const calculator = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b,
  multiply: (a, b) => a * b,
  divide: (a, b) => b !== 0 ? a / b : null
};

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy', timestamp: new Date() });
});

// Calculator endpoints
app.post('/calculate', (req, res) => {
  const { operation, a, b } = req.body;
  
  if (!operation || a === undefined || b === undefined) {
    return res.status(400).json({ error: 'Missing required parameters' });
  }
  
  if (!calculator[operation]) {
    return res.status(400).json({ error: 'Invalid operation' });
  }
  
  const result = calculator[operation](Number(a), Number(b));
  
  if (result === null) {
    return res.status(400).json({ error: 'Division by zero' });
  }
  
  res.json({ operation, a, b, result });
});

// Start server only if not in test mode
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}

module.exports = { app, calculator };