#!/usr/bin/node
class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (this.height > 0 && this.width > 0) {
      if (!c) { c = 'X'; }
      let seq = '';
      for (let index = 0; index < this.height; index++) {
        for (let index = 0; index < this.width; index++) {
          seq += c;
        }
        if (index + 1 < this.height) { seq += '\n'; }
      }
      console.log(seq);
    }
  }
}
module.exports = Square;
