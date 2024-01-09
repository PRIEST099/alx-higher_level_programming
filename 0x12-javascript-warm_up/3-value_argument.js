#!/usr/bin/node

const arr = process.argv;
if (isNaN(process.argv[2])) {
  console.log('No argument');
} else {
  console.log(arr[2]);
}
