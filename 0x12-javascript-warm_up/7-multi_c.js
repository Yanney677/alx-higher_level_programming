#!/usr/bin/node
const xtimes = parseInt(process.argv[2]);
	if (isNaN(xtimes)) {
		console.log('Missing number of occurrences')
	} else 
	for (let i = 0; i < xtimes; i++) {
		console.log('C is fun');
	}
