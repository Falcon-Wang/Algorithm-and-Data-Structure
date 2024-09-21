# 算法005：单双链表及其反转
class SinglyNode:
    """单链表结点定义"""
    def __init__(self, value=None):
        self.value = value  # 结点值
        self.next = None    # 指向下一个结点的指针

class SinglyLinkedList:
    """单向链表"""
    def __init__(self):
        self.head = None    # 链表的头结点
    
    def append(self, value):
        """在单链表末尾添加结点"""
        new_node = SinglyNode(value)
        if self.head is None:
            self.head = new_node    # 新结点成为头结点
        else:
            current = self.head     # 记录头结点
            while current.next:   # 遍历至链表末尾
                current = current.next
            current.next = new_node     # 添加新结点
    
    def traverse(self):
        current = self.head
        while current:
            print(f"{current.value} -->")
            current = current.next
        print("None")
    
    def invert(self):
        """
        单链表反转 (Leetcode 0206-Reverse Linked List)
        """
        next = None
        pre = None
        while not self.head is None:
            next = self.head.next
            self.head.next = pre
            pre = self.head
            self.head = next
        self.head = pre
        return self.head



class DoublyNode:
    """双链表结点定义"""
    def __init__(self, value=None):
        self.value = value  # 结点值
        self.next = None    # 指向下一个结点的指针
        self.prev = None    # 指向上一个结点的指针

class DoublyLinkedList:
    """双向链表"""
    def __init__(self):
        self.head = None    # 链表的头结点

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head == None:
            self.head = new_node    # 新结点成为头结点
        else:
            current = self.head     # 记录头结点
            while current.next:     # 遍历至链表末尾
                current = current.next
            current.next = new_node     # 添加指向新结点的指针
            new_node.prev = current     # 新结点的prev指针指向原尾结点
    
    def traverse(self):
        """双链表遍历"""
        current = self.head
        while current:
            print(current.value)
            current = current.next
        print("None")

    def invert(self):
        """双链表反转"""
        pass


def main():
    Singly_LinkedList = SinglyLinkedList()  # 初始化单链表
    Singly_LinkedList.append(1)     # 添加结点
    Singly_LinkedList.append(2)     # 添加结点
    Singly_LinkedList.append(3)     # 添加结点
    new_head = Singly_LinkedList.invert()
    Singly_LinkedList.traverse(new_head)    # 遍历单链表

    """
    Doubly_LinkedList = DoublyLinkedList()  # 初始化双链表
    Doubly_LinkedList.append(6) # 添加结点
    Doubly_LinkedList.append(7)
    Doubly_LinkedList.inverted_traverse()   # 倒序遍历双链表
    """
if __name__ == "__main__":
    main()