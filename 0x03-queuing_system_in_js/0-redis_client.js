import { createClient } from 'redis';

// Replace with your Redis server host and port
const redisHost = 'localhost';
const redisPort = 6379;

// Create a Redis client
const client = createClient({
  host: redisHost,
  port: redisPort,
});

// Log a message when the client connects
client.on('connect', () => {
  console.log('Connected to Redis server');
});

// Handle any errors that occur
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
