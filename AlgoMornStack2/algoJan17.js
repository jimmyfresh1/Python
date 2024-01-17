/* 
  Given a string containing space separated words
  Reverse each word in the string.

  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";



/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
let newarr=[]
let tempString=[]
let newarrarr =[]
let tempStringReverse=[]
newarr = str.split(' ')
console.log('1.' ,newarr)

for (var i = 0 ; i <newarr.length ; i++ ){
    console.log('2.',newarr[i])
    tempString=newarr[i].split('')
    console.log('3.',tempString)
    tempStringReverse= tempString.reverse()
    console.log('4.',tempStringReverse)
    var text = tempStringReverse.join('')
    console.log('test.', text)
    newarrarr.push(text)
}

return newarrarr

}
let print_var= []
print_var=reverseWords(str2) 
console.log(print_var)

/*****************************************************************************/