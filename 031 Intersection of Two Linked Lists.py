class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def length(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length

def findIntersection(firstHead, secondHead):
    firstListLength = length(firstHead)
    secondListLength = length(secondHead)

    while firstListLength > secondListLength:
        firstHead = firstHead.next
        firstListLength -= 1

    while firstListLength < secondListLength:
        secondHead = secondHead.next
        secondListLength -= 1

    while firstHead != secondHead:
        firstHead = firstHead.next
        secondHead = secondHead.next

    return firstHead

def main():
    # Test case 1
    # First linked list: 1 -> 2 -> 3 -> 4
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)

    # Second linked list: 6 -> 7 -> 8 -> 9 -> 3 -> 4
    headB = ListNode(6)
    headB.next = ListNode(7)
    headB.next.next = ListNode(8)
    headB.next.next.next = ListNode(9)
    headB.next.next.next.next = headA.next.next

    intersection = findIntersection(headA, headB)
    if intersection is not None:
        print("Intersection found at node with value:", intersection.val)
    else:
        print("No intersection found")

    # Test case 2
    # First linked list: 1 -> 2 -> 3
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)

    # Second linked list: 4 -> 5 -> 6
    headB = ListNode(4)
    headB.next = ListNode(5)
    headB.next.next = ListNode(6)

    intersection = findIntersection(headA, headB)
    if intersection is not None:
        print("Intersection found at node with value:", intersection.val)
    else:
        print("No intersection found")

if __name__ == "__main__":
    main()
