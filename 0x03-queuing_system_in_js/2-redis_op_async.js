
import { createClient, print } from 'redis';
import {promisify} from 'util';

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

const getAsync = promisify(client.get).bind(client)

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting key: ${err}`);
    } else {
      print('Reply: OK');
    }
  });
}

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch(err) {
    console.error(`Error getting value: ${err}`);
  } finally {
    client.quit();
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');