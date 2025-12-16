// test/app.test.js
const request = require('supertest');
const { app, calculator } = require('../app');

describe('Calculator API Tests', () => {
  
  describe('GET /health', () => {
    it('should return healthy status', async () => {
      const res = await request(app).get('/health');
      expect(res.statusCode).toBe(200);
      expect(res.body.status).toBe('healthy');
    });
  });

  describe('Calculator Functions', () => {
    it('should add two numbers correctly', () => {
      expect(calculator.add(5, 3)).toBe(8);
    });

    it('should subtract two numbers correctly', () => {
      expect(calculator.subtract(10, 4)).toBe(6);
    });

    it('should multiply two numbers correctly', () => {
      expect(calculator.multiply(6, 7)).toBe(42);
    });

    it('should divide two numbers correctly', () => {
      expect(calculator.divide(20, 4)).toBe(5);
    });

    it('should handle division by zero', () => {
      expect(calculator.divide(10, 0)).toBeNull();
    });
  });

  describe('POST /calculate', () => {
    it('should perform addition', async () => {
      const res = await request(app)
        .post('/calculate')
        .send({ operation: 'add', a: 10, b: 5 });
      
      expect(res.statusCode).toBe(200);
      expect(res.body.result).toBe(15);
    });

    it('should perform subtraction', async () => {
      const res = await request(app)
        .post('/calculate')
        .send({ operation: 'subtract', a: 20, b: 8 });
      
      expect(res.statusCode).toBe(200);
      expect(res.body.result).toBe(12);
    });

    it('should return 400 for invalid operation', async () => {
      const res = await request(app)
        .post('/calculate')
        .send({ operation: 'invalid', a: 5, b: 3 });
      
      expect(res.statusCode).toBe(400);
    });

    it('should return 400 for missing parameters', async () => {
      const res = await request(app)
        .post('/calculate')
        .send({ operation: 'add', a: 5 });
      
      expect(res.statusCode).toBe(400);
    });

    it('should handle division by zero gracefully', async () => {
      const res = await request(app)
        .post('/calculate')
        .send({ operation: 'divide', a: 10, b: 0 });
      
      expect(res.statusCode).toBe(400);
      expect(res.body.error).toBe('Division by zero');
    });
  });
});