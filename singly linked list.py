# Single Linked List

class Node(object): #node class
    def __init__(self, data, next=None): #생성자
        self.data = data
        self.next = next


class SList(object): #연결리스트
    def __init__(self):
        self.head = Node(None) #첫 연결리스트 생성시 data=None, next=None인 node가 한개인 연결리스트가 생성됨
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self): #연결리스트가 비어있나 없나 확인
        if self.size != 0:
            return False
        else:
            return True
    #1
    def selectNode(self, idx): #해당 노드 조회
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            target = self.head #head부터 탐색
            for cnt in range(idx): #idx
                target = target.next
            return target
    #2
    def appendleft(self, value):
        if self.is_empty(): #linked list is empty
            self.head = Node(value)
        else:
            self.head = Node(value, self.head) #head에 new node make
        self.size += 1
    #3
    def append(self, value): #end 부분에 new node make
        if self.is_empty(): #empty
            self.head = Node(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None: #end노드가 아닐 동안
                target = target.next #계속 end를 향해 move
            newtail = Node(value) #new node 생성
            target.next = newtail #end 노드에 new node연결
            self.size += 1
    #4
    def insert(self, value, idx):  #연결리스트의 중간에 새로운 노드를 insert
        # =>삽입할 자리의 앞의 노드의 next부분이 새로운 노드를 가리키게 해야하고, 새로운 노드는 이전노드가 가리키던 다음노드를 next로 가리키게 해아한다.
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        elif idx == 0: #첫 노드에 새로운 노드를 insert
            self.head = Node(value, self.head)  #old head를 new node의 next포인터가 가리키게 하고 new node 생성
            self.size += 1
        else: #중간에 노르를 insert
            target = self.selectNode(idx - 1) #first, 조회먼저^^ target은 이전노드
            if target == None:
                return
            newNode = Node(value)
            tmp = target.next
            target.next = newNode #이전노드가 new node를 가리키게 (이전노드와 다음노드의 연결고리를 끊음)
            newNode.next = tmp #new node가 다음노드를 가리키게
            self.size += 1
    #5
    def delete(self, idx):
        if self.is_empty():
            print('Underflow: Empty Linked List Error')
            return
        elif idx >= self.size:
            print('Overflow: Index Error')
            return
        elif idx == 0:
            target = self.head #target은 head노드
            self.head = target.next #head의 다음노드가 head가 된다.
            del (target) #delete
            self.size -= 1 #size--
        else:
            target = self.selectNode(idx - 1) #target은 해당 idx의 바로 전 노드
            deltarget = target.next
            target.next = target.next.next #idx의 바로 전노드와 삭제할 노드의 연결고리 끊기, target이 삭제할 노드가 가리키던 노드를 가리키게 함
            del (deltarget)
            self.size -= 1

    def printlist(self): #연결리스트 출력
        target = self.head
        while target:
            if target.next != None:
                print(target.data, '-> ', end='')
                target = target.next
            else:
                print(target.data)
                target = target.next