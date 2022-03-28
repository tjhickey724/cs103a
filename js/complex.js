class Complex{
    constructor(re,im){
	this.re=re;
	this.im=im;
    }

    add(other){
	return new Complex(this.re+other.re,this.im+other.im);
    }

    mul(other){
	let re1 = this.re*other.re -this.im*other.im;
	let im1 = this.re*other.im + this.im*other.re;
	return new Complex(re1,im1);
    }

    toString(){
	return this.re+"+"+this.im+"i"
    }

}

x = new Complex(1,1);
y = new Complex(2,3);
u = x.mul(x);
v = y.mul(y).add(x);
console.log('x=',x);
console.log('x=',x.toString());
console.log('y=',y);
console.log('u=',u);
console.log('v=',v);
    
