
const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function reverseWords(str) {
    let newarr=[]
    let word = ''
    for (var i = 0 ; i<str.length ; i++){
        console.log(str[i])
        console.log(word)
        if (str[i] == ' ' || str[i]== (str[str.length-1])){
            console.log('Im here!')
            newarr.push(word)
            console.log('test',word)
            console.log('test2',newarr)
            if (str[i]== (str[str.length-1])){
                word+=str[i]
            }
            else{
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
reverseWords(str2)