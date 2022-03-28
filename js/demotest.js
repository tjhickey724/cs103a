const mymath = require('./demo.js');
console.dir(mymath)
const x = 2;
const x2 = mymath.square(x);
const x3 = mymath.cube(x);
const x4 = mymath.sqrt(x);
const x5 = x4*x4;
console.log(`${x}^2 = ${x2}`);
console.log(`${x}^3 = ${x3}`);
console.log(`sqrt(${x}) = ${x4}`);
console.log(`(sqrt(${x})^2 = ${x5}`)

