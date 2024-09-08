#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[1], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    const decoder = new TextDecoder('utf-8');
    const fileText = decoder.decode(process.argv[1]);
    console.log(fileText);
  }
});
