/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.

  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

  const keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };
  
  const keys2 = [];
  const vals2 = [];
  const expected2 = {};
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
  function zipArraysIntoMap(keys, values) {
    // const arrTwoD = [];
    // for (var i = 0 ; i<keys.length; i++){
    //     arrTwoD[i] =[keys[i], values[i]];
    // }
    // console.log(arrTwoD)
    const arrayMap = new Map();
    for (var i=0; i<keys.length; i++){
        arrayMap.set(keys[i], values[i])
    
    }
    console.log(arrayMap)
    return arrayMap
    // code here
  }
  var container = zipArraysIntoMap(keys1, vals1)
  console.log(container)
  console.log(container.get('abc'))
  console.log(container.get(3))

  function zip(keys, values) {
    var objectMap = {}
    for (var i= 0; i<3; i++){
        var dog = keys[i]
        objectMap[dog]=values[i]
    return objectMap
    }

}
  var container2 = zip(keys1, vals1)
  console.log(container2)
  console.log(container2.abc)
  /*****************************************************************************/