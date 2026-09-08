from typing import Optional, List

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


def create_list(nums: List) -> ListNode:
    if not nums:
        return None

    head = ListNode(nums[0])
    curr = head

    for i in range(1, len(nums)):
        next = ListNode(nums[i])
        curr.next = next
        curr = next

    return head
        

def print_list(head: ListNode) -> None:
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


head = [1,2,3,4,5]
head_list = create_list(head)

s = Solution()
print_list(s.reverseList(head_list))
