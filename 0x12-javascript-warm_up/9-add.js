#!/usr/bin/node
function add(a, b) {
    const result = parseInt(a) + parseInt(b);
    console.log(result);
}

const NumArg = process.argv.slice(2);

if (NumArg.length === 2) {
    add(NumArg[0], NumArg[1]);
} else {
    console.log('NaN');
}
