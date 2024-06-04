#!/usr/bin/node

const request = require('request');
const util = require('util');
const get = util.promisify(request.get);

async function fetchCharacters () {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  try {
    const { body: film } = await get({ url, json: true });
    const characters = film.characters;

    for (let i = 0; i < characters.length; i++) {
      const { body: character } = await get({ url: characters[i], json: true });
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchCharacters();
