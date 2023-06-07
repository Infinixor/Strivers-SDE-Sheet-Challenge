# List Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getListAfterReverseOperation(head, n, b):
    # If linked list is empty, return head of the linked list.
    if head is None:
        return None

    # Variable to keep track of the current index in the block array.
    idx = 0

    cur, prev, temp = head, None, None
    tail, join = None, None
    isHeadUpdated = False

    # Reverse nodes until the list is empty or entire block array has been considered.
    while cur is not None and idx < n:
        # K represents the size of the current block.
        k = b[idx]

        # Just move to the next block if size of the current block is zero.
        if k == 0:
            idx += 1
            continue

        join = cur
        prev = None

        # Reverse nodes until end of list is reached or current block has been reversed.
        while cur is not None and k > 0:
            k -= 1
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Update the head pointer when reversing the first block.
        if not isHeadUpdated:
            head = prev
            isHeadUpdated = True

        # Tail pointer keeps track of the last node before the current k-reversed linked list.
        # We join the tail pointer with the current k-reversed linked list's head.
        if tail is not None:
            tail.next = prev

        # The tail is then updated to the last node of the current k-reversed linked list.
        tail = join
        idx += 1

    # If entire block is iterated and reached at end, then we append the remaining nodes to the tail of the partial modified linked list.
    if tail is not None:
        tail.next = cur

    # Return the head of the linked list.
    return head

def main():
    # Test case 1
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Block array: [2, 2, 2]
    b = [2, 2, 2]
    n = len(b)

    reversedHead = getListAfterReverseOperation(head, n, b)

    # Print the modified linked list after reverse operation
    while reversedHead is not None:
        print(reversedHead.data, end=" ")
        reversedHead = reversedHead.next
    print()

    # Test case 2
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Block array: [3, 1, 2]
    b = [3, 1, 2]
   
