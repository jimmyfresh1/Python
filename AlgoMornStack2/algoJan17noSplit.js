
const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function mySplit(str) {
    let newarr=[]
    let word = ''
    for (var i = 0 ; i<str.length ; i++){

        if (str[i] == ' ' || str[i]== (str[str.length-1])){
            if (str[i]== (str[str.length-1])){
                word+=str[i]
                newarr.push(word)
            }
            else{
            newarr.push(word)
            word=''
        }
        }
        else {
            word += str[i]
        }

    }
    return newarr
}
var split_test=mySplit(str2)
console.log('split test', split_test)

function myRevWord(word){
    var revWord = ''
    for (var i = (word.length-1) ; i>=0 ; i --){
        revWord += word[i]
        }
        return revWord
    }
    

// mySplit(str2)

var print_here=myRevWord('Reverseme')
console.log("rev word test", print_here)

function reverseStrings(str) {
    var newarr = []
    var finalString = ''
    newarr= mySplit(str)
    for (var i = 0 ; i<newarr.length; i++){
        let reverseWord = []
        
        reverseWord = myRevWord(newarr[i])
        if (finalString ==''){
            finalString+= reverseWord
        }
        else {
        finalString += (" " + reverseWord)

    }
    }
    return finalString
}
var final_print=reverseStrings(str2)
console.log("final test. " , final_print)