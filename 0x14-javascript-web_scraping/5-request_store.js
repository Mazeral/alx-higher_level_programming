#!/usr/bin/node

const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

req.get(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(file, body, (err) => {
      if (err) console.log(err);
    });
  }
});
