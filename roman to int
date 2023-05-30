def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
       # number = roman.fromnumeral(s)
       #return number
        #values=[1,5,10,50,100,500,1000]
        #symbols=['I','V','X','L','C','D','M']
        roman_dic={'I':1 ,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=0
        i=0

        for sym in reversed(s):

         value=roman_dic[sym]
           #if  value < i:
           #     n-=value
           #else:
           #     n+=value
           #i=value        
 
         n+=value if value >= i else -value
         i=value
        return n
