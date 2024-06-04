#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
if (!id) process.exit(1);
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(baseUrl, { json: true }, (err, resp, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data.title);
});
