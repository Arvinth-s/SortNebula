#This sort is similar to insertion sort, but is much faster than insertion sort.
#Here we dont compare only the adjacent element like insertion sort
def shell_sort(arr):
    n = len(arr)
    gap = n/2
    ele=0
    while(gap > 0):
        for i in range(gap,n):
            ele= i
            while ele > gap-1 and arr[ele] < arr[ele-gap] :
                arr[ele], arr[ele-gap] = arr[ele-gap], arr[ele]
                ele-=gap
        gap /=2
    print arr

def main():
    arr=[]
    arr_num = int(raw_input("type number of array").strip())
    for i in range (arr_num):
        arr.append(list(map(int, raw_input("Type key and value for hash table").split())))
    shell_sort(arr)

if __name__ == "__main__":
    main()

    
    
