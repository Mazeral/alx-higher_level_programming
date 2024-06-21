#!/usr/bin/node
const data = require('./101-data.js').dict;

function transformObject (obj) {
  const transformed = {};
  Object.keys(obj).forEach(key => {
    const value = obj[key];
    if (!transformed[value]) { transformed[value] = []; }
    transformed[value].push(key);
  });
  return transformed;
}
const dict = transformObject(data);
console.log(dict);
