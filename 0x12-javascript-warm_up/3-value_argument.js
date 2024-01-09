#!/usr/bin/node

const arr = process.argv;
if (process.argv[2] === null) {
  console.log('No argument');
} else {
  console.log(arr[2]);
}
