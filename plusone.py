
def plusOne( digits):
            
        digits = digits[::-1]  # Reverse the list
        carry = 1

        for i in range(len(digits)):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.append(carry)

        return digits[::-1] 

testcase = [[9]]       
for lst in testcase:
        print("Original List:", lst)
        updated_list = plusOne(lst)
        print("Updated List:", updated_list)
        print()
