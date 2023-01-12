/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    // Define step counter
    let steps = 0
    
    // While loop since we have a condition to fulfill and iterations is variable
    while(num > 0){
        // Increment step counter
        steps++
        
        // Test if num is even
        if(num % 2 == 0){
            num /= 2
        } else {
            num -= 1
        }
    }
    return steps
    
};