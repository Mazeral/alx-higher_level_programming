#!/usr/bin/node
if (process.argv.slice(2) == 0) {
	console.log("No argument")
}
else
process.argv.slice(2).forEach(val => {
	console.log(val);
});
