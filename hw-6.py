def check_AB_BA(string):
    result = "NO"
    
    if "AB" in string:
    
        if "BA" in string[string.index("AB")+2:]:
            result = "YES"
    
    if "BA" in string:
        
        if "AB" in string[string.index("BA")+2:]:
            result = "YES"
    
    return result

print(check_AB_BA("ABBA")) 
print(check_AB_BA("BAAB")) 
print(check_AB_BA("ABA")) 
print(check_AB_BA("ABHA")) 
