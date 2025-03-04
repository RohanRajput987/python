class Solution:
    def mergealternatelystr(self,word1,word2):
        result=[]
        i=0
        while len(word1)>i or len(word2)>i:
            if len(word1)>i:
                result.append(word1[i])
            if len(word2)>i:
                result.append(word2[i])
            i+=1
        return "".join(result)
word1=input("Enter the First String : ")
word2=input("Enter the Second String : ")
print(Solution().mergealternatelystr(word1,word2))
