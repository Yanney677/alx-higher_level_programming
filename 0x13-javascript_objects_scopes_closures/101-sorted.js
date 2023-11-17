#!/usr/bin/node
/* a script that imports a dictionary of occurrences by user id and 
 computes a dictionary of user ids by occurrence.
 */

const dict = require('./101-data').dict;

const tolist = Object.entries(dict);
const val = Object.values(dict);
const UniqVals = [...new Set(val)];
const newDict = {};
for (const m in UniqVals) {
  const list = [];
  for (const n in tolist) {
    if (tolist[n][1] === UniqVals[m]) {
      list.unshift(tolist[n][0]);
    }
  }
  newDict[UniqVals[m]] = list;
}
console.log(newDict);
