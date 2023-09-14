#!/usr/bin/node
const argsArray = Array.from(arguments).map(Number);
if (argsArray.length <= 1) {
  console.log(0);
}
const sortedArgs = argsArray.sort((a, b) => b - a);
console.log(sortedArgs[1]);
