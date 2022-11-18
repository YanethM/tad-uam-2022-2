class Tree:
    class Csll:
        class Node:
            def __init__(self, value, father):
                self.value = value
                self.father = father
                self.son = None
                self.next = None
        def __init__(self):
            self.head = None  
            self.tail = None
            self.length = 0
        def append(self, value, father):
            new_node = self.Node(value, father)
            if self.head == None and self.tail == None:
                self.head = new_node
                self.tail = new_node
                self.tail.next = self.head
            else:
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node
            self.length += 1
    def __init__(self):
        self.raiz = None
        self.length = 0
    def insert(self, value, father):
        if self.raiz == None:
            self.raiz = self.Csll()
            self.raiz.append(value, None)
        else:
            current_node = self.raiz.head
            def tree_route(node, node_puebra=None):
                node_aux = node.father
                if value == father:
                    return False
                elif node.value == father:
                    if node.son ==  None:
                        node.son = self.Csll()
                        node.son.append(value, node)
                        self.length += 1
                        return True
                    else:
                        node.son.append(value, node)
                        self.length += 1
                        return True
                else:
                    if node.son != None:
                        if node.son.head.value == node_puebra:
                            if node.value == self.raiz.head.value:
                                return False
                            elif node.next.value != node_aux.son.head.value:
                                return tree_route(node.next, node.value)
                            else: 
                                return tree_route(node.father, node.next.value)
                        else:
                            return tree_route(node.son.head, node.son.head.value)
                    elif node.next.value != node_aux.son.head.value:
                        return tree_route(node.next, node.value)
                    else:
                        return tree_route(node.father, node.next.value)
            return tree_route(current_node)

    def find(self, value):
        current_node = self.raiz.head
        def tree_route(node, node_puebra=None):
            node_aux = node.father
            #El nodo es el padre
            if node.value == value:
                return node.value
            #El nodo tiene un hijo
            elif node.son != None:
                if node.son.head.value == node_puebra:
                    if node.value == self.raiz.head.value:
                        return " >>>> No existe el nodo buscado <<<<"
                    elif node.next.value != node_aux.son.head.value:
                        return tree_route(node.next, node.value)
                    else: 
                        return tree_route(node.father, node.next.value)
                else:
                    return tree_route(node.son.head, node.son.head.value)
            elif node.next.value != node_aux.son.head.value:
                return tree_route(node.next, node.value)
            else:
                return tree_route(node.father, node.next.value)
        find_node = tree_route(current_node)
        return print(find_node)
    def preorder(self):
        visited_nodes = []
        current_node = self.raiz.head
        def tree_route(node, node_puebra=None):
            node_aux = node.father
            if node.son != None:
                if node.son.head.value == node_puebra:
                    if node.value == self.raiz.head.value:
                        return None
                    elif node.next.value != node_aux.son.head.value:
                        return tree_route(node.next, node.value)
                    else: 
                        return tree_route(node.father, node.next.value)
                else:
                    visited_nodes.append(node.value)
                    return tree_route(node.son.head, node.son.head.value)
            elif node.next.value != node_aux.son.head.value:
                visited_nodes.append(node.value)
                return tree_route(node.next, node.value)
            else:
                visited_nodes.append(node.value)
                return tree_route(node.father, node.next.value)
        tree_route(current_node)
        return print(visited_nodes)
    def postorder(self):
        visited_nodes = []
        current_node = self.raiz.head
        def tree_route(node, node_puebra=None):
            node_aux = node.father
            if node.son != None:
                if node.son.head.value == node_puebra:
                    visited_nodes.append(node.value)
                    if node.value == self.raiz.head.value:
                        return None
                    elif node.next.value != node_aux.son.head.value:
                        return tree_route(node.next, node.value)
                    else: 
                        return tree_route(node.father, node.next.value)
                else:
                    return tree_route(node.son.head, node.son.head.value)
            elif node.next.value != node_aux.son.head.value:
                visited_nodes.append(node.value)
                return tree_route(node.next, node.value)
            else:
                visited_nodes.append(node.value)
                return tree_route(node.father, node.next.value)
        tree_route(current_node)
        return print(visited_nodes)
