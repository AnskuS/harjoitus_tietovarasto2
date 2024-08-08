def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        print(f'array: {arr}')
        print(f'm: {mid}')

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
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
    value_list = [1, 5, 6, 8, 9, 23, 33, 51, 54, 57, 78]
    print(f'value_list: {value_list}')
    sorted_list = merge_sort(value_list)
    print(f'Sorted list: {sorted_list}')