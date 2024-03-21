// server.js

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const port = 3000;

// Enable CORS for cross-origin requests
app.use(cors());

// MongoDB setup
mongoose.connect('mongodb://localhost:27017/your-database-name', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Create a mongoose model for your shipment data
const Shipment = mongoose.model('Shipment', {
  shipmentNumber: String,
  routeDetails: String,
  device: String,
  poNumber: String,
  ndcNumber: String,
  serialNumber: String,
  containerNumber: String,
  goodsType: String,
  expecteddate: String,
  deliveryNumber: String,
  batchid: String,
  shipmentdesc: String,
});

// API endpoint to fetch shipment data
app.get('/api/shipments', async (req, res) => {
  try {
    const shipments = await Shipment.find();
    res.json(shipments);
  } catch (error) {
    console.error('Error fetching shipments:', error);
    res.status(500).send('Error fetching shipments. Please try again later.');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
