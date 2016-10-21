'use strict';

function sortArr(arr1) {
	var counter = 0;
	var arr2 = arr1.slice();
	arr1.sort(function(a,b){
		return a-b;
	});

	Number(arr1);
	console.log(arr2);
	console.log(arr1);

	for (var i=0; i<arr1.length; i++){
		if (arr2[i] !== arr1[i]){
			counter++;
		}
	}

	return counter;
}

var myArray = [];

for (var j=0; j<15; j++){
	var num = Math.floor(Math.random()*100);
	myArray.push(num);
}

var a = sortArr(myArray);
console.log(a);


