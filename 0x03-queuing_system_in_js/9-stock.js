import { createClient } from 'redis';
const express = require('express');
import { promisify } from 'util';
const app = express();

const PORT = 1245;

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

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const listProducts = [
    {itemId: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    {itemId: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    {itemId: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    {itemId: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
]

const getItemById = (id) => {
    const product =  listProducts.find(obj => obj.itemId === id);
    if (product) {
        return Object.fromEntries(Object.entries(product));
      };
}

const reserveStockById = async(id, stock) => {
    const result = await setAsync(`item.${id}`, stock);
    return result;
}

const getCurrentReservedStockById = async(id) => {
    const product = await getAsync(`item.${id}`);
    return product;
}


app.get('/list_products', (_req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
    const id = Number.parseInt(req.params.itemId);
    const product = getItemById(id);
    if (!product) {
        res.json({"status":"Product not found"});
        return;
    }
    getCurrentReservedStockById(id)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
        product.currentQuantity = product.initialAvailableQuantity - reservedStock;
        res.json(product);
    })
});

app.get('/reserve_product/:itemId', (req, res) => {
    const id = Number.parseInt(req.params.itemId);
    const product = getItemById(id);
    if (!product) {
        res.json({"status":"Product not found"});
        return;
    }
    getCurrentReservedStockById(id)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
        if (reservedStock >= product.currentQuantity) {
            res.json({"status":"Not enough stock available","itemId":id})
        } else {
            reserveStockById(id, reservedStock + 1);
            product.currentQuantity = product.initialAvailableQuantity - 1;
            res.json({"status":"Reservation confirmed","itemId":id})
        }
    })
})

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
})
