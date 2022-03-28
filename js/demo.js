// demo package
const square = x => x*x;
function cube(x) { return x*x*x;}
const sqrt = (x) => 
   {g=1; 
    for(let i=0; i<100; i++){
        g= (g+x/g)/2
    } 
    return g}
module.exports = {square,cube,sqrt}; // shorthad for {square:square,cube:cube,sqrt:sqrt}
