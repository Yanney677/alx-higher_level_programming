#!/usr/bin/node
const NumArg = parseInt(process.argv[2]);

if (Number.isNaN(NumArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < NumArg; i++) {
    let row = '';
    for (let j = 0; j < NumArg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
