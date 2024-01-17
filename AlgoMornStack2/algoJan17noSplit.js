
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
        console.log(str[i])
        console.log(word)
        if (str[i] == ' ' || str[i]== (str[str.length-1])){
            if (str[i]== (str[str.length-1])){
                word+=str[i]
                newarr.push(word)
            }
            else{
            console.log('Im here!')
            newarr.push(word)
            console.log('test',word)
            console.log('test2',newarr)
            word=''
        }
        }
        else {
            word += str[i]
        }
        console.log(newarr)

    }
    
    console.log(newarr)
    return newarr
}

function myRevWord(word){
    var revWord = ''
    for (var i = (word.length-1) ; i>=0 ; i --){
        revWord += word[i]
        }
        return revWord
    }
    

// mySplit(str2)

var print_here=myRevWord('TESTESTE')
console.log(print_here)

function reverseStrings(str) {
    var newarr = []
    var finalString = ''
    newarr= mySplit(str)
    for (var i = 0 ; i<newarr.length; i++){
        let reverseWord = []
        
        reverseWord = myRevWord(newarr[i])
        finalString += (" " + reverseWord)
        console.log(reverseWord)
    }
    return finalString
}
var final_print=reverseStrings(str2)
console.log(final_print)