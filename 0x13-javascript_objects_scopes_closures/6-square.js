#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let seq = '';
      for (let index = 0; index < this.height; index++) {
        for (let index = 0; index < this.width; index++) {
          seq += 'X';
        }
        if (index + 1 < this.height) { seq += '\n'; }
      }
      console.log(seq);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

class Square extends Rectangle {
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
