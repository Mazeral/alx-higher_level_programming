#!/usr/bin/node
if (process.argv.slice(2).length === 0) {
  console.log('No argument');
} else {
  if (process.argv.slice(2).length === 1) { console.log('Argument found'); }

  if (process.argv.slice(2).length > 1) { console.log('Arguments found'); }
}
