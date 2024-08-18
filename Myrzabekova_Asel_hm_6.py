#1. Написать функцию bubble_sort или selection_sort, принимающую в качестве входящего параметра не отсортированный список.
#2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# я выбрала фукцию bubble_sort

def bubble_sort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break
    return list


#4. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором необходимо искать.

def binary_search(sorted_list_bubble, target):
    ResultOk = False
    Pos = -1
    First = 0
    Last = len(sorted_list_bubble) - 1

    while First <= Last: #condition #1
            Middle = (First + Last) // 2 #calculate Middle
            if sorted_list_bubble[Middle] == target:
                Pos = Middle
                ResultOk = True
                break
            elif sorted_list_bubble[Middle] < target: #if target is greater than Middle
                First = Middle + 1
            else:
                Last = Middle - 1 # if target is less than Middle


    if ResultOk:
        print('Element is found')
        print("Target:", target)
        print("Position:", Pos)
    else:
        print("Element is not found")

#3. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию
unsorted_list = [101, 25, 206, 13, 2, 1003, 56, 62, 271]
sorted_list_bubble = bubble_sort(unsorted_list.copy())
print("Bubble Sort:", sorted_list_bubble)

target = 101

binary_search(sorted_list_bubble, target)

#5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.


#6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию