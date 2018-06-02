def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p = head
    q = head
    while p and q and q.next:
        p = p.next
        q = q.next.next
        if p == q:
            p2 = p
            q2 = head
            while p2 != q2:
                p2 = p2.next
                q2 = q2.next
            return p2

def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    nodes = set()
    while head:
        if head in nodes:
            return head
        nodes.add(head)
        head = head.next
    return None