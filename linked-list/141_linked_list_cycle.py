def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None or head.next is None:
        return False
    p = head;
    q = head.next;
    while p != q :
        if q is None or q.next is None:
            return False
        p = p.next
        q = q.next.next
    return True