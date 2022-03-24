# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        now = ans = ListNode()  # 空的開頭
        while list1 and list2:
            if list1.val < list2.val:
                now.next = list1
                list1 = list1.next
            else:
                now.next = list2
                list2 = list2.next
            now = now.next
            #print(now.val)

        if list1:
            now.next = list1
        else:
            now.next = list2
        return ans.next


s = Solution()
l3 = ListNode(val=5, )
l2 = ListNode(val=2, next=l3)
l1 = ListNode(val=1, next=l2)
k3 = ListNode(val=4, )
k2 = ListNode(val=3, next=k3)
k1 = ListNode(val=1, next=k2)
s.mergeTwoLists(l1, k1)
