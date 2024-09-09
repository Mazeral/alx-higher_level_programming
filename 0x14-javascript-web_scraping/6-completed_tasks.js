#!/usr/bin/node

const request = require('request');

const api_url = process.argv[2];

request(api_url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const completedTasks = data.filter(task => task.completed);
  const tasksByUser = {};

  for (const task of completedTasks) {
    if (!tasksByUser[task.userId]) {
      tasksByUser[task.userId] = 1;
    } else {
      tasksByUser[task.userId]++;
    }
  }
	console.log(tasksByUser)

});
