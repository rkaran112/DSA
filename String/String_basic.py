class Basics:
    def getLength(self,string)->int:
        cnt = 0
        for i in string:
            cnt+=1
        return cnt

    def searchCharIndex(self,s,target)->int:
        for i in range(len(s)):
            if s[i] == target:
                return i
        return -1
    def subString(self,s,substr)->bool:
        n = len(s)
        m = len(substr)
        for i in range(n-m+1):
            match = True
            for j in range(m):
                if s[i+j]!=substr[j]:
                    match = False
                    break
            if match:
                return True
        return False
    def palinDrome(self,s: str)->bool:
        s = s.lower()
        clean = ""
        for i in s:
            if i.isalnum():
                clean +=i
        left = 0
        right = len(clean)-1
        while left<right:
            if clean[left]!= clean[right]:
                return False
            left +=1
            right -=1
        return True
    
    def isAnagram(self,s,t)->bool:
        if len(s)!=len(t):
            return False
        catch ={}
        for i in s:
            catch[i] = catch.get(i,0)+1
        for i in t:
            if catch.get(i,0)<=0:
                return False
            catch[i] -=1
        return True
    
    
bas = Basics()
s= "Was it a car or a cat I saw?"
# print(bas.getLength(s))
# print(bas.searchCharIndex("akjfsnakjdio","a"))
print(bas.palinDrome("Was it a car or a cat I saw?"))
# print(s.isalnum())    