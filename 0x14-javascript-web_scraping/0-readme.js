#!/usr/bin/node

const fs = require('fs');

const path = process.argv[1]
fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    const decoder = new TextDecoder('utf8');
    const fileText = decoder.decode(data);
    console.log(fileText);
  }
});
