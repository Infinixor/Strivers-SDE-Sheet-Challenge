
"""
@author:  Infinixor 

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def firstNode(head):
    if head is None:
        return None

    slow = head
    fast = head

    while True:
        if fast and fast.next:
            fast = fast.next.next
        else:
            return None
        slow = slow.next
        if fast == slow:
            break

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None

    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

def main():
    # Test case with a cycle
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next.next  # Creating a cycle at node 4
    result = firstNode(head)
    if result is None:
        print("No cycle detected")
    else:
        print("First node of the cycle:", result.data)

# Run the main method
if __name__ == "__main__":
    main()
