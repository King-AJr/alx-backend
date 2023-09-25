import { createClient } from 'redis';
import { promisify} from 'util';

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

const hsetAsync = promisify(client.hset).bind(client);
const hgetallAsync = promisify(client.hgetall).bind(client)

const setHashField = async (key, field, value) => {
    try {
      const result = await hsetAsync(key, field, value);
      console.log('Reply: 1');
    } catch (error) {
      console.error(`Error setting hash field: ${error}`);
    } finally {
      client.quit();
    }
  }

const getHashField = async(key) => {
    try {
        const result = await hgetallAsync(key);
        console.log(result);
    } catch (error) {
        console.error(`Error getting hash field: ${error}`)
    } finally {
        client.quit()
    }
}
setHashField('HolbertonSchools', 'Portland', '50');
setHashField('HolbertonSchools', 'Seattle', '80');
setHashField('HolbertonSchools', 'New York', '20');
setHashField('HolbertonSchools', 'Bogota', '20');
setHashField('HolbertonSchools', 'Cali', '40');
setHashField('HolbertonSchools', 'Paris', '2');
getHashField('HolbertonSchools');
