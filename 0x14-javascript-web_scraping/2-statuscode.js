#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + resp.statusCode);
});
