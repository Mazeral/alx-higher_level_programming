#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    // parsing is important!!!
    console.log(JSON.parse(body).title);
  }
});
