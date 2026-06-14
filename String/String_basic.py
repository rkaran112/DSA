class Basics:
    def getLength(self,string)->int:
        cnt = 0
        for i in string:
            cnt+=1
        return cnt

    def searchCharIndex(self,s,target,goal)->int:
        seen = set()
        for i in range(len(s)):
            if s[i] == target:
                seen.add(i)
        return seen
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
                    True
    # def palindrome(self,s,substr)->bool:
    #     break
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
            catch[i] = catch.get(i,0)
        for i in t:
            if catch==t[i]:
                catch[i] -=1
            if catch[i]<0:
                return False
            return True
    
    
bas = Basics()
s= "Was it a car or a cat I saw?"
# print(bas.getLength(s))
# print(bas.searchCharIndex("akjfsnakjdio","a"))
print(bas.palinDrome("Was it a car or a cat I saw?"))
# print(s.isalnum())    