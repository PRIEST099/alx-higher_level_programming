#!/usr/bin/node

const arr = process.argv;
if (arr === undefined) {
  console.log('No argument');
} else {
  console.log(arr[2]);
}
