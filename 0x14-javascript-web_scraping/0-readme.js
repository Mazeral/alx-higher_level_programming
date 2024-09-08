#!/usr/bin/node

const fs = require('fs');

console.log(process.argv[1]);
fs.readFile(process.argv[1], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    const decoder = new TextDecoder('utf-8');
    const fileText = decoder.decode(data);
    console.log(fileText);
  }
});
