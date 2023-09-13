#!/usr/bin/node
function factorial (number) {
  if (isNaN(parseInt(number))) {
    return 1;
  } else if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const argument = parseInt(process.argv[2]);
console.log(factorial(argument));
