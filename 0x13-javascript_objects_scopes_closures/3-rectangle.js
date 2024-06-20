#!/snap/bin/node
// #!/usr/bin/node
class Rectangle {
	constructor(w, h){
		if (w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}
	print(){
		let seq = "";
		for (let index = 0; index < this.height; index++) {
			for (let index = 0; index < this.width; index++) {
				seq += "#"	
			}
			seq += ""
		}
		console.log(seq);
	}
};

module.exports.Rectangle = Rectangle;
