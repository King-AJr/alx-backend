import { createClient, print } from 'redis';

// Replace with your Redis server host and port
const redisHost = 'localhost';
const redisPort = 6379;
const channel = 'holberton school channel';

// Create a Redis client
const client = createClient({
  host: redisHost,
  port: redisPort,
});

const publisher = createClient({
  host: redisHost,
  port: redisPort,
});

// Log a message when the client connects
client.on('connect', () => {
  console.log('Connected to Redis server');
  client.subscribe(channel);
});

// Handle any errors that occur
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Handle incoming messages on the subscribed channel
client.on('message', (subscribedChannel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER' && subscribedChannel === channel) {
    client.unsubscribe(subscribedChannel);
    client.quit();
  }
});