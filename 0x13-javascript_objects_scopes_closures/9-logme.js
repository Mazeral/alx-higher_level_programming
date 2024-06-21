#!/usr/bin/node
exports.logMe = function (item) {
  if (typeof exports.logMe.cnt === 'undefined') {
    exports.logMe.cnt = 0;
  }
  console.log(`${exports.logMe.cnt}: ${item}`);
  exports.logMe.cnt++;
};
