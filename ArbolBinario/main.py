"""
1, 10, 3, 14, 12, 9, 7, 8, 19
"""
from binary_search_tree import ArbolBinario

add = ArbolBinario()

add.add(1)
add.add(10)
add.add(3)
add.add(14)
add.add(12)
add.add(4)
add.add(9)
add.add(7)
add.add(8)
add.add(19)

# add.show_in_order(add.root)
# add.show_pos_order(add.root)
add.show_pre_order(add.root)

# print(add.search(add.root, 14).parent.value)

# los codigos tre primeros son para ordenarlos de diferentes formas

# print(add.search(add.root, 1).value) este codigo es para buscar el valor
# print(add.search(add.root, 1).left) este codigo es para ver si es hijo izquierdo
# print(add.search(add.root, 1).right) este codigo es para ver si es hijo derecho
# print(add.search(add.root, 1).parent.value) este codigo es para ver cual es su padre

"""
en orden
# 1, 3, 4, 7, 8, 9, 10, 12, 14, 19

Pos orden
# 8, 7, 9, 4, 3, 12, 19, 14 ,10, 1

Pre orden
# 1, 10, 3, 4, 9, 7, 8, 14, 12, 19
"""