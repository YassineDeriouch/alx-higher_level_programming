#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(0);
} else {
  const nbMax = process.argv.slice(2).sort((a, b) => b - a);
  console.log(nbMax[nbMax.length - 3]);
}
