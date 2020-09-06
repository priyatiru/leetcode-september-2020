myDict={}
        res=[]        
        p1=0
        p2=0
        windowStart=float('inf')
        windowEnd=0
        
        for idx, char in enumerate(S): #saving the rightmost index of each char
            myDict[char]=idx 
        
        while p2<len(S):  
            p2=max(p2,myDict[S[p1]]) 
            windowEnd=max(windowEnd,p2)
            windowStart=min(p1,windowStart)
            
            if p1==p2 or p2==len(S)-1: # when p1=p2 end of first substring or P2=end so must append to res and restart windowStart and windowEnd and increment p2 to be=new start of substring
                res.append(windowEnd-windowStart+1)
                windowStart=float('inf')
                windowEnd=0
                p2+=1 
                    
            p1+=1 #in all cases we move p1
            
        return res