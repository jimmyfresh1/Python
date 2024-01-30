/* 
Recursive Sigma

Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
let count = 0;
let sum = 0;
function recursiveSigma(num) {
    num = Math.floor(num)
    if(count >= num){
        return 0
    }
    else{
    // return num + recursiveSigma(num-1)
    count++
    sum += count 
    console.log(sum)
    return recursiveSigma(num)
    }
}
recursiveSigma(num1)
recursiveSigma(num2)
recursiveSigma(num3)

/*****************************************************************************/