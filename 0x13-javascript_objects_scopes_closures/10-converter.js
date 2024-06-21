#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    number.toString(base);
  };
};
