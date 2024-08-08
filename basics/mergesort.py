def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину списка
        L = arr[:mid]  # Делим элементы на две половины
        R = arr[mid:]

        print(f'array: {arr}')
        print(f'm: {mid}')

        merge_sort(L)  # Сортируем первую половину
        merge_sort(R)  # Сортируем вторую половину

        i = j = k = 0

        # Копируем данные во временные массивы L и R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print(f'Merging...')
        print(f'left: {L}')
        print(f'right: {R}')
        print(f'merged: {arr}')
    return arr

if __name__ == '__main__':
    input_str = "1,5,6,8,9,23,33,51,54,57,78"
    input_list = list(map(int, input_str.split(',')))
    print(f"Enter numbers, separated by ',': {input_str}")
    print(f"input_list: {input_list}")
    sorted_list = merge_sort(input_list)
    print(f'Sorted list: {sorted_list}')