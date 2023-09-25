import { createClient, print } from 'redis';

// Replace with your Redis server host and port
const redisHost = 'localhost';
const redisPort = 6379;
const channel = 'holberton school channel';

const publisher = createClient({
  host: redisHost,
  port: redisPort,
});


const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish(channel, message);
  }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);