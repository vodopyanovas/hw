'use strict';

var arr = [];

for (var i=1; i<101; i++){
	arr.push(i);	
}

for (var n in arr){
	if (arr[n] % 3 == 0){
		if(arr[n] % 5 == 0){		
			console.log('FizzBuzz');
		}
		console.log('Fizz');
	}

	else {		
		arr[n] % 5  ? console.log(arr[n]) : console.log('Buzz') ;
	}
}