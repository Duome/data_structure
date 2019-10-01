# -*- coding: utf-8 -*-
"""
数据结构——
线性数据结构——
    栈——
        创建栈（不包含数据项）                                    Stack()
        加入栈项（无返回值）                                      push(item)
        将数据项移除（返回栈顶的数据，并且栈被修改）                   pop()
        窥视栈顶数据项（返回栈顶的数据,但不移除该数据项，并且栈不被修改）  peek()
        判断栈是否为空（为空返回True，不为空返回False）               isEmpty()
        查询栈中多少个数据项（返回栈中有多少数据项）                   size()
    队列——
        创建空队列（返回队列对象）               Queue()
        添加数据项（无返回值）                  enqueue(item)
        移除数据项（返回队首数据项，队列被修改）    dequeue()
        判断是否为空队列（返回布尔值）            isEmpty()
        数据大小（返回数据项个数）               size()
    双端队列——
        创建双端队列                      Deque()
        添加队首数据项（无返回值）           addFront(item)
        添加队尾数据项（无返回值）           addRear(item)
        移除队首数据项（返回移除的数据项）     removeFront()
        移除队尾数据项（返回移除的数据项）     removeRear()
        判断双端队列是否为空（返回布尔值）     isEmpty()
        查询双端队列大小（返回数据项个数）     size()
    链表——
        创建空列表（返回对象）                        List()
        添加数据项（返回空，假设item原不存在与表中）      add(item)
        移除某个数据项（返回移除数据项，列表被修改）       remove(item)
        判断是否存在数据项（返回布尔类型值）              search(item)
        判断是否为空（返回布尔值）                      isEmpty()
        查询数据大小（返回数据项大小）                   size()
        添加末尾数据项（返回空，假设item原先不存在与列表）  append(item)
        查询数据索引（返回数据项在表中的位置）            index(item)
        插入数据项（返回空）                          insert(pos, item)
        移除末尾数据项（返回移除数据项，列表被修改）       pop()
        移除某位数据项（返回移除数据项，列表被修改）       pop(pos)
"""

# 栈——队首进队首出，列尾进列尾出
class Stack(object):
    def __init__(self):
        self.stack_list = []

    # 添加数据
    def push(self, item):
        self.stack_list.append(item)

    # 移除数据
    def pop(self):
        if not self.isEmpty():
            return self.stack_list.pop()

    # 查询数据
    def peek(self):
        if not self.isEmpty():
            return self.stack_list[-1]

    # 判断是否为空栈
    def isEmpty(self):
        return self.stack_list == []

    # 查询数据大小
    def size(self):
        return len(self.stack_list)


# 队列——队尾进队首出，列首进列
class Queue(object):
    def __init__(self):
        # 创建队列
        self.queue_list = []

    def enqueue(self, item):
        # 添加数据项
        self.queue_list.insert(0, item)

    def dequeue(self):
        # 移除数据项
        if not self.isEmpty():
            return self.queue_list.pop()

    def isEmpty(self):
        # 判断是否为空队列
        return self.queue_list == []

    def size(self):
        # 查询队列大小
        return len(self.queue_list)


# 双端队列——首末两端都可以进出
class Deque(object):
    def __init__(self):
        # 创建双端队列
        self.deque_list = []

    def addFront(self, item):
        # 添加队首数据项
        self.deque_list.append(item)

    def addRear(self, item):
        # 添加队尾数据项
        self.deque_list.insert(0, item)

    def removeFront(self):
        # 移除队首数据项
        if not self.isEmpty():
            return self.deque_list.pop()

    def removeRear(self):
        # 移除队尾数据项
        if not self.isEmpty():
            return self.deque_list.pop(0)

    def isEmpty(self):
        # 判断是否为空双端队列
        return self.deque_list == []

    def size(self):
        # 查询队列大小
        return len(self.deque_list)


class List(object):
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.insert(0, item)

    def remove(self, item):
        self.list.remove(item)

    def search(self, item):
        return item in self.list

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)

    def append(self, item):
        self.list.append(item)

    def index(self, item):
        return self.list.index(item)

    def insert(self, pos, item):
        self.list.insert(pos, item)

    def pop(self, item=False):
        if not self.isEmpty():
            if item:
                return self.list.pop(item)
            else:
                return self.list.pop()



if __name__ == '__main__':
    data = Stack()
    data.push(1)
    data.push(2)
    data.pop()
    data.peek()
    data.isEmpty()
    data.size()




















