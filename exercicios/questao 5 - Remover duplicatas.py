def remover_duplicatas(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

minha_lista = [1, 2, 3, 4, 4, 3, 1, 5, 6, 5, 7]
nova_lista = remover_duplicatas(minha_lista)
print(nova_lista)
