#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  construcor (size) {
    super(size, size);
  }
};
