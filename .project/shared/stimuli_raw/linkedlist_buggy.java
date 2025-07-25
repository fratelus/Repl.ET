public void insertAtEnd(ListNode head, int value) {
    ListNode newNode = new ListNode(value);
    
    if (head == null) {
        head = newNode;
        return;
    }
    
    ListNode current = head;
    // Bug: missing null check before accessing next
    while (current.next != null) {
        current = current.next;
    }
    
    current.next = newNode;
} 