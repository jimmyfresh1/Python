/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    // var temp =[str[0]]
    var tempstring =''
    for (var i = 1; i <str.length; i++) {
        for (const char of tempstring){
        if (char !== str[i]){
            tempstring += str[i]
            
        }
        
    }
    console.log(tempstring)}
    return tempstring
}
strprint = stringDedupe(str1)
console.log(strprint)

/*****************************************************************************/