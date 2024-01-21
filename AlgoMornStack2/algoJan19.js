str1= "Helloworld!"

function rotateStr(str, amnt) {
    // create a counter to check the amount
    let count = amnt;
    let newStr = ''
    // while amount it greater then 0 it will run what is in the loop.
    for (let i = 0; i < str.length; i++) {
      while (count > 0) {
        newStr[i] = str[i + 1];
        console.log("test", newStr)
        count--;
        
      }
    }
    return str
  }
  /*****************************************************************************/
  console.log(rotateStr(str1, 5))