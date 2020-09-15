pattern_list=[]
string_pattern={}

#takes input for the pattern
pattern=input("Enter the pattern\n")

#takes input for the string
string=input("Enter the string\n")

def pattern_matching(string,pattern) :
    string=string.split(" ")
    if len(pattern) != len(string) :
        return 0
    for i in range(len(string)) :
        if string[i] not in string_pattern.keys() :
            if pattern[i] in pattern_list :
                return 0
            pattern_list.append(pattern[i])
            string_pattern[string[i]]=pattern[i]
        else :
            if pattern[i] != string_pattern[string[i]] :
                return 0
    return 1

pat_str=pattern_matching(string,pattern)

if pat_str == 1 :
    print(True)
else :
    print(False)
