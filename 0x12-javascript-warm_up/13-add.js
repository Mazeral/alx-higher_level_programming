#!/usr/bin/node
function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);
  return (num1 + num2);
}

module.exports.add = add;
