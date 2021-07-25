import math

separator = ""
def mergeSort(alist):
#    print("Splitting ",alist)
   if len(alist)>1:
       mid = math.ceil(len(alist)/2)
       lefthalf = alist[:mid]
       righthalf = alist[mid:]
       global separator
       separator += "|"
       temp = separator
       print(f"{lefthalf} {separator} {righthalf}")
       #recursion
       mergeSort(lefthalf)
       separator = temp
       mergeSort(righthalf)
    #    print(f"{lefthalf} | {righthalf}")

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
   if len(alist) != 1:
    print("Merging ",alist)

alist = [523, 126, 67, 1, 500, 34, 21, 229, 9, 123, 13]
inp = input("Input array with spaces between elements: ")
inp = inp.replace(",", "")
alist = inp.split()
alist = list(map(lambda x: int(x), alist))
mergeSort(alist)
print(alist)