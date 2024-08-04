# Реалізація класу вузла однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Реалізація класу однозв'язного списку
class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання вузла до списку
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Друк списку
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Завдання 1.1: Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Завдання 1.2: Функція сортування однозв'язного списку вставками
    def sortedInsert(self, node):
        if self.head is None or self.head.data >= node.data:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next is not None and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node

    def insertionSort(self):
        sorted_head = None
        current = self.head
        while current is not None:
            next = current.next
            sorted_head = self.sortedInsert(Node(current.data))
            current = next
        self.head = sorted_head

    # Завдання 1.3: Функція об'єднання двох відсортованих однозв'язних списків
    def mergeLists(self, head1, head2):
        dummy = Node(0)
        tail = dummy
        while head1 is not None and head2 is not None:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1 is not None:
            tail.next = head1
        if head2 is not None:
            tail.next = head2
        return dummy.next

# Приклади використання функцій
if __name__ == "__main__":
    # Приклад використання реверсування
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    print("Список до реверсування:")
    llist.printList()
    llist.reverse()
    print("Список після реверсування:")
    llist.printList()

    # Приклад використання сортування вставками
    llist = LinkedList()
    llist.push(30)
    llist.push(3)
    llist.push(4)
    llist.push(20)
    print("Список до сортування:")
    llist.printList()
    llist.insertionSort()
    print("Список після сортування:")
    llist.printList()

    # Приклад використання об'єднання списків
    llist1 = LinkedList()
    llist1.push(15)
    llist1.push(10)
    llist1.push(5)

    llist2 = LinkedList()
    llist2.push(20)
    llist2.push(3)
    llist2.push(2)

    llist1.head = llist1.mergeLists(llist1.head, llist2.head)
    print("Об'єднаний відсортований список:")
    llist1.printList()
