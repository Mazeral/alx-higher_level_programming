#!/usr/bin/node
const source1 = process.argv[2];
const source2 = process.argv[3];
const dest = process.argv[4];
const src1 = readFile(source1);
const src2 = readFile(source2);
