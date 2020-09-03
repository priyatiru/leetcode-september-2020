class Solution:
    def repeatedSubstringPattern(self,s:str) -> bool:
        rep=''
        length_s=len(s)
        for i in range(length_s//2):    #to check half of the substring
            rep+= s[i]                  #we have to add whatever is present in the string
            if length_s % len(rep) ==0:   #to check if the substring is possible

                # multiply rep with a certain number which is gonna 
                # make it as same length as our string 
                if rep * (length_s// len(rep)) == s:
                    return True
        return False
