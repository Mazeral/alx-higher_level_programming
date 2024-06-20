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
	rotate(){
		const tmp = this.width;
		this.width = this.height;
		this.height = tmp;
	}
	double()
	{
		this.height = this.height * 2;
		this.width = this.width * 2;
	}

};

class Square extends Rectangle{
	constructor(size)
	{
		super(size,size);
	}
}
module.exports.Square = Square;
