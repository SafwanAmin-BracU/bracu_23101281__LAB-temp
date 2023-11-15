class Node:
    def __init__(self, elem, next_node=None) -> None:
        self.data = elem
        self.next = next_node

    def __repr__(self) -> str:
        return repr(self.data)


# Sample Input 1:
# [1, 2, 3, 4, 5], 3
# Sample Output 1:
# [3, 2, 1, 4, 5]

# Sample Input 2:
# [1, 2, 3, 4, 5], 5
# Sample Output 2:
# [5, 4, 3, 2, 1]

# Sample Input 3:
# [1, 2, 3, 4, 5], 1
# Sample Output 3:
# [1, 2, 3, 4, 5]


def reverseUptoN(head: Node, n: int) -> Node:
    if n <= 1:
        return head
    current = head
    for i in range(n - 1):
        current = current.next
    tail = current.next

    return head


def createLinkedList(arr: list) -> Node:
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head


def printLinkedList(head: Node) -> None:
    temp = head
    arr = []
    while temp:
        arr.append(temp.data)
        temp = temp.next
    print(*arr, sep="->")


if __name__ == "__main__":
    linked_list = createLinkedList([1, 2, 3, 4, 5])
    print("Original Linked List:")
    printLinkedList(linked_list)
    print()

    print("Test-1:")
    print("Expected:", end=" ")
    print("3->2->1->4->5")
    print("Actual:", end=" ")
    printLinkedList(reverseUptoN(linked_list, 3))

    print("Test-2:")
    print("Expected:", end=" ")
    print("5->4->3->2->1")
    print("Actual:", end=" ")
    printLinkedList(reverseUptoN(linked_list, 5))

    print("Test-3:")
    print("Expected:", end=" ")
    print("1->2->3->4->5")
    print("Actual:", end=" ")
    printLinkedList(reverseUptoN(linked_list, 1))

    print("Test-4:")
    print("Expected:", end=" ")
    print("1->2->3->4->5")
    print("Actual:", end=" ")
    printLinkedList(reverseUptoN(linked_list, 0))
