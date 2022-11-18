from SingleLikedList import SingleLinkedList

inst_sll = SingleLinkedList()

''' E,D,A,B,C'''
inst_sll.push_node('C')
inst_sll.push_node('A')
inst_sll.push_node('2')
inst_sll.push_node(True)
inst_sll.push_node('B')
inst_sll.show_info_sll()
#print(inst_sll.get_node_value(4))
print(inst_sll.update_node_value(4,'Valor nuevo'))
inst_sll.show_info_sll()
print('--------------------------------')
inst_sll.remove_node(5)
inst_sll.show_info_sll()




