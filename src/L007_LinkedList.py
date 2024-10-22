# 算法007：单双链表及其反转
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
        while self.head is not None:
            next = self.head.next
            self.head.next = pre
            pre = self.head
            self.head = next
        self.head = pre
        return self.head
    
    def merge_linked_list(list1: SinglyNode, list2: SinglyNode):
        """合并两个有序单链表, 使合并后的单链表整体有序"""
        # 检查链表是否为空
        if list1 is None or list2 is None:
            return list2 if list1 is None else list1
        
        # 确定头结点更小的子链表
        head: SinglyNode = list2 if list1.value > list2.value else list1

        curr1: SinglyNode = head.next
        curr2: SinglyNode = list1 if head is list2 else list1
        pre = head

        while curr1 is not None and curr2 is not None:
            if curr1.value <= curr2.value:
                pre.next = curr1
                curr1 = curr1.next
            else:
                pre.next = curr2
                curr2 = curr2.next
            pre = pre.next
        pre.next = curr1 if curr1 is not None else curr2

        return head

        



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
            print(f"{current.value} -->")
            current = current.next
        print("None")

    def invert(self):
        next = None
        prev = None
        while self.head is not None:
            next = self.head.next
            self.head.next = prev
            self.head.prev = next
            prev = self.head
            self.head = next
        self.head = prev


def main():

    linked_list_1 = SinglyLinkedList()
    linked_list_1.append(1)
    linked_list_1.append(3)
    linked_list_1.append(5)
    
    linked_list_2 = SinglyLinkedList()
    linked_list_2.append(2)
    linked_list_2.append(4)
    linked_list_2.append(6)
    
    # 合并两个有序链表，并输出结果
    merged_head = SinglyLinkedList.merge_linked_list(linked_list_1.head, linked_list_2.head)
    
    # 打印合并后的链表
    merged_list = SinglyLinkedList()
    merged_list.head = merged_head
    merged_list.traverse()
    
if __name__ == "__main__":
    main()