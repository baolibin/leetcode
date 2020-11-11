# coding:utf-8
'''
剑指 Offer 22. 链表中倒数第k个节点

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pre = head
        later = head
        for i in range(k):
            pre = pre.next
        while pre:
            pre = pre.next
            later = later.next
        return later

# 另外一种方法
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        result = []
        while head:
            result.append(head)
            head = head.next
        return result[-k]