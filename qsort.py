def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = []
        right = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        return quick_sort(left) + [pivot] + quick_sort(right)
def main():
    
    unsorted_list = input("Enter a list of numbers: ").split()
    unsorted_list = [int(x) for x in unsorted_list]
    
    
    sorted_list = quick_sort(unsorted_list)
    print(f"The sorted list is: {sorted_list}")

main()
