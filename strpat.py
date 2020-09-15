pattern_list=[]
string_pattern={}

#takes input for the pattern
pattern=input("Enter the pattern")

#takes input for the string
string=input("Enter the string")

def pattern_matching(string,pattern) :
    string=string.split(" ")
    if len(pattern) != len(string) :
        return print(False)
    for i in range(len(string)) :
        if string[i] not in string_pattern.keys() :
            if pattern[i] in pattern_list :
                return print(False)
            pattern_list.append(pattern[i])
            string_pattern[string[i]]=pattern[i]
        else :
            if pattern[i] != string_pattern[string[i]] :
                return print("False")
    return print(True)

pattern_matching(string,pattern)