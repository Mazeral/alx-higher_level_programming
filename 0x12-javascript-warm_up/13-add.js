#!/snap/bin/node
// #!/usr/bin/node
function add(a, b) {
	num1 = parseInt(a);
	num2 = parseInt(b);
	return (num1 + num2);
}

module.exports.add = add
