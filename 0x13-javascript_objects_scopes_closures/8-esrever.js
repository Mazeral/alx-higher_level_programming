#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length;
  const reversed = [];
  for (let index = size - 1; index > -1; index--) {
    reversed.push(list[index]);
  }
  return reversed;
};
