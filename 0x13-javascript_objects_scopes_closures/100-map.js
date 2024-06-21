#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const result = list.map((item, index) => {
  return (parseInt(item) * parseInt(index)
  );
});
console.log(result);
