#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];
// writes the content by default
fs.writeFile(filePath, content, (err) => {
  if (err) console.log(err);
});
