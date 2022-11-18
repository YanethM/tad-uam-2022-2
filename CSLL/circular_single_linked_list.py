class CircularSingleLinkedList:

    class Node:
        #Método inicializador clase Node
        def __init__(self,value):
            self.value = value
            self.next = None

    #Método inicializador clase CircularSingleLinkedList
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #Método para imprimir los valores de los nodos
    def show_list(self):
        circular_list = []
        current_node = self.head
        pivote = True
        contador = self.length
        #Mientras en la lista al menos exista un nodo
        while contador != 0:
            if pivote != False or current_node != self.head:
                circular_list.append(current_node.value)
                current_node = current_node.next
                pivote = False
                contador -=1 
            else:
                break
        print(circular_list)

    #Añadir nodo al inicio de la lista
    def unshift_node(self, value):
        new_node = self.Node(value)
        #Caso en el que no existen nodos en la lista
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        #Caso en el que al menos existe un nodo
        else:
            self.tail.next = new_node
            new_node.next = self.head  
            self.head = new_node
        self.length += 1

    def append_node(self, value):
        new_node = self.Node(value)
        #Caso en el que no existen nodos en la lista
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        #Caso en el que al menos existe un nodo
        else:
            self.tail.next = new_node
            new_node.next = self.head  
            self.tail = new_node
        self.length += 1
    
    #Eliminar el primer nodo de la lista
    def shift_node(self):
        if self.length > 0:
            remove_node = self.head
            self.head = remove_node.next
            self.tail.next = self.head
            remove_node.next = None
            print(remove_node.value)
            self.length -= 1
        else:
            #if self.length == 0:
            self.head = None
            self.tail = None
            self.length = 0






