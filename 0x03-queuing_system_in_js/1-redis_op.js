
import { createClient, print } from 'redis';

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

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting key: ${err}`);
    } else {
      print('Reply: OK');
    }
  });
}

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(`Error getting value: ${err}`);
    } else {
      console.log(value)
    }
  })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');