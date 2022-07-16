class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

# first_node = Node(21)
# print(f"first node - {first_node}")
# print(f"first node - {first_node.value}")
# print(f"first node - {first_node.next}")

# second_node = Node("Timmy Shar")
# print(f"second node - {second_node}")
# print(f"second node - {second_node.value}")

class SLL:
    def __init__(self,head = None):
        self.head = head

    # add to back
    def AddToBack(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next 
        runner.next = new_node
        return self

    def display(self):
        str_node = ""
        node_num = 1
        runner = self.head
        while runner: # same as while runner != none 
            str_node += f'the value of the {node_num} node is {runner.value} '
            node_num += 1
            runner = runner.next
        print(str_node)
        return self

# first_sll = SLL(Node(21))

# first_sll.AddToBack(51).AddToBack(71).AddToBack(7).AddToBack(45)

# print(first_sll.head.value) # print head

# print(first_sll.head.next) # print 2nd node space in memory

# print(first_sll.head.next.value) # print 2nd node

# first_sll.display() # using a runner to display all node values 


class_SLL = SLL()
class_SLL.AddToBack("homer simpson im not sam").AddToBack(99).display()
