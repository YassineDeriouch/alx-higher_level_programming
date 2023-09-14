#!/usr/bin/node

const dictInput = require('./101-data').dict;
const DictOutput = {};

for (const key in dictInput) {
  const ocurr = dictInput[key];
  DictOutput[ocurr] = [];
  for (const keys in dictInput) {
    if (dictInput[keys] === ocurr) {
      DictOutput[ocurr].push(keys);
    }
  }
}
console.log(DictOutput);
