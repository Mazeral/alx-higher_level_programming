#!/usr/bin/node
if (process.argv.slice(2)[0] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv.slice(2)[0]);
}
