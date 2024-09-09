#!/usr/bin/node

const req = require('request');

const url = process.argv[2];

let count = 0;
req.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    // parsing the body
    const data = JSON.parse(body);
    // going through the data
    for (let i = 0; i < data.results.length; i++) {
      // getting every character array of every film
      const charUrl = data.results[i].characters;
      for (let index = 0; index < charUrl.length; index++) {
        // getting the id
        const charId = parseInt(charUrl[index].split('/')[5]);
        if (charId === 18) { count++; }
      }
    }
  }
  // count
  console.log(count);
});
