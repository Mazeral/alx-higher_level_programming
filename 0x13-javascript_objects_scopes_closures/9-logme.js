#!/usr/bin/node
exports.logMe = function (item) {
  logMe.cnt = 0;
  console.log(`${cnt}: ${item}`);
  logMe.cnt++;
};
