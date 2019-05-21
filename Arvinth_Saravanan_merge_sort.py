#since time is the most important factor in the probem, i opt to use mergesort since the time complexity is nlogn(small)
#understanding algorithm: Merge_sort is direct implementation of divide and conquer strategy
#the given array is divided into two and the two sub-arrays are in turn divided into two each
#Process continues till the size of both the arrays reaches 1. Now sorting starts and sorted array are merged from back to front
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)/2 #Each time the given array is divided into two 
        L = arr[:mid] 
        R = arr[mid:] 

        mergeSort(L)   # first the left part is continuously divided into two
        #At this point the left part is completely divided into elemetns while the right side is untouched
        mergeSort(R) # This now point to the array of length 2 or 1 ( depending upon the n value) 
  
        i = j = k = 0 # sorting is done again at each steps
          
        #sorting starts
        while i < len(L) and j < len(R): #normal procedure to add the elements from two sorted arrays
            if L[i] < R[j]: 
                arr[k] = L[i] #copying least of two values
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        #When elements from one array has completely been added and there are some elements left in the other arrays
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i]," ") 
    print() 
def main():
    arr=[]
    arr_count = int(raw_input("enter the number of elements in hash table").strip())
    for i in range(arr_count):
        arr.append(list(map(int, raw_input("enter the key and value" ).rstrip().split())))
    print ("Given array is", arr)  
    mergeSort(arr) 
    print("Sorted array is: ") 
    printList(arr) 

# driver code to test the above code 
if __name__ == '__main__':
    main()







"""
                                            ***********Flow of command**********

                                        if an array consists of eight elements
                                                            ABCDEFGH
                                                    ABCD             EFGH
                                                 AB      CD       EF      GH
                                               A   B   C   D     E  F    G  H
Now B and A are sorted in AB and C and D are sorted in CD. This continues from bottom to up to complete the sorting process

                                                                    1,28
                            2,8,14                                                                            15,21,27
        
                    3,5,7                        9,11,13                               16,18,20                                             22,24,26

                 4         6                    10      12                           17         19                                       13              25

This diagram represents the array pointed in flow of command. As we can see the right hand side is split at final stages.
                                        
                                               
                

            
"""
