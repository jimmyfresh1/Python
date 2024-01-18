str1 = "Y(3(p)p(3)r)s"
#expected1 = True

str2 = "N(0(p)3"
#expected2 = False
# Explanation: not every parenthesis is closed.


str3 = "N(0)t ) 0(k"
#expected3 = False
#Explanation: because the second ")" is premature: there is nothing open for it to close.

str4 = "a(b))(c"
#expected4 = False

def parens_valid(str):
    #make variables to store the counts of open and close parenthesis
    open_count = 0
    close_count = 0
    for character in str: 
        #console.log(character);
        if character == "(":
            open_count += 1
        
        if character ==")":
            close_count += 1
        
        if close_count > open_count:
            #check if the count of closing parenthesis is greater than # of opening parenthesis return false
            return False
        
    #check the numbers of open and count if the number even out at the end of the loop
    if( (open_count + close_count) % 2 != 0):
        return False
    
    return True


print(parens_valid(str1))
print(parens_valid(str2))
print(parens_valid(str3))
print(parens_valid(str4))