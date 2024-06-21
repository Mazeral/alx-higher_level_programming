#!/usr/bin/node
const size = parseInt(process.argv[2]);
let output = '';
if (!size) { console.log("Missing size"); } else {
  for (let index = 0; index < size; index++) {
    for (let index = 0; index < size; index++) {
      output += '#';
    }
    if ((index + 1) < size) { output += '\n'; }
  }
  console.log(output);
}
