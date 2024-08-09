#HÉBER PEREIRA GARCIA
import math
import time
import random

####### Selection sort
def selectionSort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i+1, len(arr)):
            if arr[min_indx] > arr[j]:
                min_indx = j  
        arr[i], arr[min_indx] = arr[min_indx], arr[i]

####### insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

####### mergesort
def merge_sort(arr):
    if len(arr) > 1:
    
        meio = len(arr) // 2
        parteEsquerda = arr[:meio]
        parteDireita = arr[meio:]
    
        merge_sort(parteEsquerda)
        merge_sort(parteDireita)
        i = k = j = 0
 
        while i < len(parteEsquerda) and j < len(parteDireita):
            if parteEsquerda[i] < parteDireita[j]:
                arr[k] = parteEsquerda[i]
                i += 1
            else:
                arr[k] = parteDireita[j]
                j += 1
            k += 1

        while i < len(parteEsquerda):
            arr[k] = parteEsquerda[i]
            i += 1
            k += 1

        while j < len(parteDireita):
            arr[k] = parteDireita[j]
            j += 1
            k += 1

####### Heap Sort
def heapify(arr, n, i):
      maior = i
      esq = 2 * i + 1
      dire = 2 * i + 2
  
      if esq < n and arr[i] < arr[esq]:
          maior = esq
  
      if dire < n and arr[maior] < arr[dire]:
          maior = dire
  
      if maior != i:
          arr[i], arr[maior] = arr[maior], arr[i]
          heapify(arr, n, maior)
  
  
def heapSort(arr):
      n = len(arr)
  
      #Criar o maxHeap
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
  
      for i in range(n-1, 0, -1):
          #Troca
          arr[i], arr[0] = arr[0], arr[i]
  
          heapify(arr, i, 0)

####### QuickSort

def quickSort(arr):
    # Função principal do QuickSort
    if len(arr) <= 1:
        return arr

    # Escolhe o pivo como a mediana dos três primeiros, três do meio e três últimos elementos
    indice_meio = len(arr) // 2
    pivo = mediana_de_tres(arr[0], arr[indice_meio], arr[-1])

    # Cria 3 vetores, ao dividir o array
    esquerda, igual, direita = particionar(arr, pivo)

    # Ordena recursivamente
    return quickSort(esquerda) + igual + quickSort(direita)

def mediana_de_tres(a, b, c):
    # Calcula a mediana
    return sorted([a, b, c])[1]

def particionar(arr, pivo):
    # Divide o array em três partes
    esquerda, igual, direita = [], [], []
    for num in arr:
        if num < pivo:
            esquerda.append(num)
        elif num == pivo:
            igual.append(num)
        else:
            direita.append(num)
    return esquerda, igual, direita

####### Couting sort

def counting_Sort(arr):
    # Encontra o valor máximo no array de entrada para determinar o tamanho do array count.
    maior_valor = max(arr)
    size = len(arr)
    output = [0] * size
    #Cria e inicializa o array count.
    count = [0] * (maior_valor + 1)
    #No array count, mantém o controle de quantos de cada valor existem.
    for num in arr:
        count[num] += 1
    #Mantém o controle do número total de contagens acumuladas.
    for i in range(1, maior_valor + 1):
        count[i] += count[i - 1]
    #No array count, encontra o índice de cada elemento do array original e os coloca os elementos no array de saída.
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
    #Copia os elementos ordenados de volta para o array original.
    for i in range(size):
        arr[i] = output[i]

####### ESTRUTURA PRINCIPAL DO CÓDIGO
inc = 1000
fim = 20000
stp = 1000
rpt = 10

metodos_ordenacao = [selectionSort, insertion_sort, merge_sort, heapSort, quickSort, counting_Sort]
print("[[RANDOM]]")
print("   n   | selection Sort |  | Insertion Sort |   | Merge Sort |     | Heap Sort |        | Quick Sort |      | Counting sort |")
print("-" * 125)

#Criando vetores para os casos de teste
while inc <= fim:
    select = []
    insert = []
    merg = []
    heap = []
    quick = []
    counting = []

    metodos = [select, insert, merg, heap, quick, counting]
    
    i = 0
#para criar os vetores especificos aqui para todos os tipos de ordenação
    while i <= rpt:
        vetor = list(range(0, inc))
        random.shuffle(vetor)
        row = f"{inc:<11}"

        j = 0
        for method in metodos_ordenacao:
            vetor_copia = vetor.copy()
            tempo_inicial = time.time()
            method(vetor_copia)
            tempo_final = time.time()
            tempo_execucao = tempo_final - tempo_inicial

            metodos[j].append(tempo_execucao)
            j+=1

        i += 1

#Calcular a média de tempo de execução do algortimo
    x = 0
    while x < len(metodos_ordenacao):
        for y in metodos[x]:
            y += y
        media = y/rpt
        row += f"{media:.6f}{' ':<12}"
        x +=1

    print(row)
    inc = inc + stp
print() 

#--------------------------VETOR REVERSO-------------------------------------

inc = 1000
fim = 20000
stp = 1000
rpt = 10

metodos_ordenacao = [selectionSort, insertion_sort, merge_sort, heapSort, quickSort, counting_Sort]

print("[[REVERSED]]")
print("   N   | selection Sort |  | Insertion Sort |   | Merge Sort |     | Heap Sort |        | Quick Sort |      | Counting sort |")
print("-" * 125)

#Criando vetores para os casos de teste
while inc <= fim:
    select = []
    insert = []
    merg = []
    heap = []
    quick = []
    counting = []

    metodos = [select, insert, merg, heap, quick, counting]
    
    i = 0
#para criar os vetores especificos aqui para todos os tipos de ordenação
    while i <= rpt:
        vetor = list(range(0, inc))
        vetor.reverse()
        row = f"{inc:<11}"

        j = 0
        for method in metodos_ordenacao:
            vetor_copia = vetor.copy()
            tempo_inicial = time.time()
            method(vetor_copia)
            tempo_final = time.time()
            tempo_execucao = tempo_final - tempo_inicial

            metodos[j].append(tempo_execucao)
            j+=1

        i+= 1
#Calcular a média de tempo de execução do algortimo
    x = 0
    while x < len(metodos_ordenacao):
        for y in metodos[x]:
            y += y
        media = y/rpt
        row += f"{media:.6f}{' ':<12}"
        x +=1
    print(row)
    inc = inc + stp
print()

#-----------------VETOR ORDENADO------------------------
inc = 1000
fim = 20000
stp = 1000
rpt = 10

metodos_ordenacao = [selectionSort, insertion_sort, merge_sort, heapSort, quickSort, counting_Sort]

print("[[SORTED]]")
print("   N   | selection Sort |  | Insertion Sort |   | Merge Sort |     | Heap Sort |        | Quick Sort |      | Counting sort |")
print("-" * 125)

#Criando vetores para os casos de teste
while inc <= fim:
    select = []
    insert = []
    merg = []
    heap = []
    quick = []
    counting = []

    metodos = [select, insert, merg, heap, quick, counting]
    
    i = 0
#para criar os vetores especificos aqui para todos os tipos de ordenação
    while i <= rpt:
        vetor = list(range(0, inc))
        row = f"{inc:<11}"

        j = 0
        for method in metodos_ordenacao:
            vetor_copia = vetor.copy()
            tempo_inicial = time.time()
            method(vetor_copia)
            tempo_final = time.time()
            tempo_execucao = tempo_final - tempo_inicial
            metodos[j].append(tempo_execucao)
            j+=1

        i+= 1
#Calcular a média de tempo de execução do algortimo
    x = 0
    while x < len(metodos_ordenacao):
        for y in metodos[x]:
            y += y
        media = y/rpt
        row += f"{media:.6f}{' ':<12}"
        x +=1
    print(row)
    inc = inc + stp
print()

#-------------NEARLY SORTED------------------

inc = 1000
fim = 20000
stp = 1000
rpt = 10

metodos_ordenacao = [selectionSort, insertion_sort, merge_sort, heapSort, quickSort, counting_Sort]

print("[[NEARLY SORTED]]")
print("   N   | selection Sort |  | Insertion Sort |   | Merge Sort |     | Heap Sort |        | Quick Sort |      | Counting sort |")
print("-" * 125)

#Criando vetores para os casos de teste
while inc <= fim:
    select = []
    insert = []
    merg = []
    heap = []
    quick = []
    counting = []

    metodos = [select, insert, merg, heap, quick, counting]
    
    i = 0
#para criar os vetores especificos aqui para todos os tipos de ordenação
    while i <= rpt:
        vetor = list(range(0, inc))
        #Criando um vetor semi-ordenado ao "embaralhar" alguns termos
        qtd_embaralhar = int(0.1 * inc)
        for l in range (qtd_embaralhar):
            vlr1 = random.randint(0, inc - 1)
            vlr2 = random.randint(0, inc - 1)
            vetor[vlr1], vetor[vlr2] = vetor[vlr2], vetor[vlr1]    
        row = f"{inc:<11}"

        j = 0
        for method in metodos_ordenacao:
            vetor_copia = vetor.copy()
            tempo_inicial = time.time()
            method(vetor_copia)
            tempo_final = time.time()
            tempo_execucao = tempo_final - tempo_inicial
            metodos[j].append(tempo_execucao)
            j+=1

        i+= 1
#Calcular a média de tempo de execução do algortimo
    x = 0
    while x < len(metodos_ordenacao):
        for y in metodos[x]:
            y += y
        media = y/rpt
        row += f"{media:.6f}{' ':<12}"
        x +=1
    print(row)
    inc = inc + stp
