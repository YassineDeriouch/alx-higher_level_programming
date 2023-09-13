#!/usr/bin/node
function factorial (nbr) {
  return nbr === 0 || isNaN(nbr) ? 1 : nbr * factorial(nbr - 1);
}
console.log(factorial(Number(process.argv[2])));
