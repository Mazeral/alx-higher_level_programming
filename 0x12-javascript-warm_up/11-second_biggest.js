#!/usr/bin/node
const arr = process.argv.slice(2);
const numarr = arr.map(str => parseInt(str, 10));
const sorted = numarr.sort((a, b) => a - b);
console.log(numarr[sorted.length - 2]);
