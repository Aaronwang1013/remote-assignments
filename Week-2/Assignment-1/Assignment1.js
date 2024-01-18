function max(numbers){
    if (numbers.length < 0){
        console.log("your array need at least 1 element")
        return 0;
    } else {
        max_number = numbers[0];
    }
    for (i = 0; i < numbers.length ; i++){
        if (numbers[i] > max_number){
            max_number = numbers[i]
        }
    }
    return max_number
}

function findPosition(numbers, target) {
    for (i = 0 ; i < numbers.length ; i++){
        if (numbers[i] == target) {
            return i
            }
        }
        return -1
    }
   


console.log( max([1, 2, 4, 5]) );
console.log( max([5, 2, 7, 1, 6]) );


console.log( findPosition([5, 2, 7, 1, 6], 5) );
console.log( findPosition([5, 2, 7, 1, 6], 7) ); 
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) );
console.log( findPosition([5, 2, 7, 1, 6], 8) );