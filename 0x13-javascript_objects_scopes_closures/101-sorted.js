#!/usr/bin/node
const data = require('./101-data.js').dict;

function transformObject (obj) {
  const transformed = {};

  // Iterate over each key in the original object
  Object.keys(obj).forEach(key => {
    // Get the value corresponding to the current key
    const value = obj[key];

    // If the value is not yet in the transformed object, initialize it as an empty array
    if (!transformed[value]) {
      transformed[value] = [];
    }

    // Push the current key into the array corresponding to its value
    transformed[value].push(key);
  });

  return transformed;
}
const dict = transformObject(data);
console.log(dict);
