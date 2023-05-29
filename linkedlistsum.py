class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)  # Dummy head node for the result list
    curr = dummy_head
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        curr.next = ListNode(carry % 10)
        curr = curr.next
        carry //= 10

    return dummy_head.next


# Take input for linked list 1
l1 = None
num_values = int(input("Enter the number of values for linked list 1: "))
for _ in range(num_values):
    value = int(input("Enter a value for linked list 1: "))
    if l1 is None:
        l1 = ListNode(value)
        curr = l1
    else:
        curr.next = ListNode(value)
        curr = curr.next

# Take input for linked list 2
l2 = None
num_values = int(input("Enter the number of values for linked list 2: "))
for _ in range(num_values):
    value = int(input("Enter a value for linked list 2: "))
    if l2 is None:
        l2 = ListNode(value)
        curr = l2
    else:
        curr.next = ListNode(value)
        curr = curr.next

# Call the function to add the two linked lists
output = addTwoNumbers(l1, l2)

# Print the result
while output:
    print(output.val, end=" ")
    output = output.next
