class Solution(object):
    def isPalindrome(self, x):
        num=x
        reverse=0
        if(x<0):
            return False
        else:
            while x>0:
                unit=x%10
                reverse=reverse*10+unit
                x=x//10
                
        if(num==reverse):
            return True
        else:
            return False
            
x=121
print(Solution().isPalindrome(x))


            
        
