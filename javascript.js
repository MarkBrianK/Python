function fizzBuzz(n){
    let result = [];
    for(let i = 1; i<=n; i++){
        let add ='';
        
        if(i % 3 === 0){
            add +='Fizz';

        }
        if ( i % 5 === 0){
            add += 'Buzz';
        }
        if (add === ''){
            result.push(i);
        }
        else{
            result.push(add);
        }
    }
    return result;
}

