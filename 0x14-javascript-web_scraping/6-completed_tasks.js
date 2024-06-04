#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
if (!url) process.exit(1);
request(url, { json: true }, (err, resp, data) => {
  if (err) {
    console.log(err);
    return;
  }

  const taskCompleted = {};
  data.forEach((todo) => {
    if (todo.completed) {
      if (!taskCompleted[todo.userId]) {
        taskCompleted[todo.userId] = 1;
      } else {
        taskCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(taskCompleted);
});
