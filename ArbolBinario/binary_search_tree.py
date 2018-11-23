from node import Node

class ArbolBinario:
    def __init__(self):
        self.root = None

    def empty(self):
        if self.root == None:
            return True
        else:
            return False
    def add(self, value):
        if self.empty():
            self.root = Node(value=value, is_root=True)
        else:
            node = self.__get_place(value)
            if value <= node.value:
                node.left = Node(value=value, parent=None, is_left=True)
            else:
                node.right = Node(value=value, parent=node, is_right=True)

    def __get_place(self, value):
        aux = self.root
        while aux:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp

    def show_in_order(self, node):

        if node:
            self.show_in_order(node.left)
            print(node.value)
            self.show_in_order(node.right)

    def show_pre_order(self, node):

        if node:
            print(node.value)
            self.show_pre_order(node.left)
            self.show_pre_order(node.right)

    def show_pos_order(self, node):

        if node:
            self.show_pos_order(node.left)
            self.show_pos_order(node.right)
            print(node.value)

    def search(self, node, value):
        if node == None:
            return None
        else:
            if node.value == value:
                return node
            elif value <= node.value:
                return self.search(node.left, value)
            else:
                return self.search(node.right, value)