// const str = "a x a";
// const expected1 = true;

// const str2 = "racecar";
// const expected2 = true;

// const str3 = "Dud";
// const expected = false;

// const str4 = "oho!";
// const expected4=false;

// function palinDrome () 

/* 
  String: Is Palindrome

  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
    var splitString = str.split("") // splits the string into an explicit array
    console.log('splitString', splitString)
    var reverseArray = splitString.reverse() // reverses the same array and then assigns to a new variable
    console.log('reverseArray', reverseArray)
    var joinArray = reverseArray.join("") // puts it back together
    console.log(joinArray)
    if (str === joinArray) // checks if the two strings are equivalent 
    {
    return true
    }
    else 
    {
        return false 
    }
}
var test1 =isPalindrome(str3)
console.log(test1)

//   var reverseString1=isPalindrome(str1)
//   if (reverseString1 == str1) {
//     print("true")
//   }
//   else {
//     print("false")
//   }
