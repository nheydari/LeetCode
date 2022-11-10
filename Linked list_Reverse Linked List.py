class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None) :
            return head
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
