var arr1 = [];
var arr2 = [];
var numb = 123;
var string = 'abc';

console.log('arr1:\n')

for (var i = 0; i<50; i++){
	var rand = Math.floor(Math.random()*2);
	rand > 0 ? arr1[i] = string : arr1[i] = numb;	
	console.log(arr1[i]);
}

console.log('\narr2:\n')
for (var j=0; j<50; j++){
	arr1[j] > 0 ? arr2[j] = arr1[j] : arr2[j] = 8;
	console.log(arr2[j]);
}