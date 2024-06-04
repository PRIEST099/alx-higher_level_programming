#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const data = process.argv[3];
if (!path || !data) process.exit(1);
fs.writeFile(path, data, 'utf8', (err) => {
  if (err) console.log(err);
});
