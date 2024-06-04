#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
if (!url || !path) process.exit(1);
const stream = fs.createWriteStream(path, { encoding: 'utf8' });
const req = request(url);
req.on('error', (err) => console.log(err));
req.on('response', (resp) => {
  resp.pipe(stream);
});
