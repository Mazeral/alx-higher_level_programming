#!/snap/bin/node
// #!/usr/bin/node
function callMeMoby(x, action)
{
	for (let index = 0; index < x; index++) {
		action();
	}
}
module.exports.callMeMoby = callMeMoby;
