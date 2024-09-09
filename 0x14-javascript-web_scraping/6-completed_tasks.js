#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const completedTasks = data.filter(task => task.completed);
  const tasksByUser = {};

  for (const task of completedTasks) {
    // looks like incrementing an element increment it's pair, not the key
    if (!tasksByUser[task.userId]) {
      tasksByUser[task.userId] = 1;
    } else {
      tasksByUser[task.userId]++;
    }
  }
  console.log(tasksByUser);
});
