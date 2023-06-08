from sys import stdin
import sys

"""
@author:  Infinixor 

"""
sys.setrecursionlimit(10 ** 7)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

left = None

def isPalindrome(head):
    global left
    left = head
    isPal = isPalindromeUtil(head)
    return isPal

def isPalindromeUtil(right):
    global left
    if right is None:
        return True
    isPal = isPalindromeUtil(right.next)
    if not isPal:
        return False
    if left.data == right.data:
        isSame = True
    else:
        isSame = False
    left = left.next
    return isSame

def takeinput():
    inputlist = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentData in inputlist:
        if currentData == -1:
            break
        Newnode = Node(currentData)
        if head is None:
            head = Newnode
            tail = Newnode
        else:
            tail.next = Newnode
            tail = Newnode
    return head
