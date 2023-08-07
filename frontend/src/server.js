const express = require("express");
const http = require("http");
const os = require("os");
const app = express();
const port = 8080; // You can change this to any desired port number
// Serve static files from the "public" folder
app.use(express.static("public"));
// Route for the homepage
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/opt/app/index.js");
});
// Create the HTTP server
const server = http.createServer(app);
// Get the local IP address for the LAN
const interfaces = os.networkInterfaces();
let localIP = "localhost";
for (const key in interfaces) {
  for (const iface of interfaces[key]) {
    if (iface.family === "IPv4" && !iface.internal) {
      localIP = iface.address;
      break;
    }
  }
}
// Start the server
server.listen(port, () => {
  console.log(`Web app is running on http://${localIP}:${port}`);
});