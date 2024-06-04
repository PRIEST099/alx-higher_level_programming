#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
if (!url) process.exit(1);
request(url, { json: true }, (err, resp, data) => {
  if (err) {
    console.log(err);
    return;
  }
  let found = 0;
  const movies = data.results;
  for (const movie of movies) {
    for (const c of movie.characters) {
      if (c === 'https://swapi-api.alx-tools.com/api/people/18/') {
        found++;
      }
    }
  }
  console.log(found);
});
