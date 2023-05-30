class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        return x == x[::-1]
number = 12321
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")

  
        """
        l=digits[-1]+1
        digits[-1]=l

        if digits[-1]>9:
            last,ones=divmod(digits[-1],10)
            digits[-1]=last
            digits.append(ones)
        else:
           digits[-1]=l   
     
        return digits   
        '''
       
       ''' 
       if len(digits)>0:

            digits[-1]+=1

            for i in range(len(digits)-1,0,-1):
                if digits[i]>9:
                    digits[i]%=10
                    digits[i-1]+=1
        
        if digits[0]> 9:
            digits[0]%=10
            digits.insert(0,1)  

        return digits    '''
           
       """            
        
        

    
