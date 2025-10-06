import matplotlib.pyplot as plt
import time
import random

def random_list(n):
    mylist=[]
    for i in range(n):
        mylist.append(random.randint(0,10000))
    return mylist


def merge(left,right):
    merged=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(mylist):
    if len(mylist)<=1:
        return mylist
    mid=len(mylist)//2
    left_sort=merge_sort(mylist[:mid])
    right_sort=merge_sort(mylist[mid:])
    return merge(left_sort,right_sort)


def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        key=mylist[i]
        j=i-1 
        while j>=0 and mylist[j]>key:
            mylist[j+1]=mylist[j]
            j-=1
        mylist[j+1]=key
    return mylist


def hybrid_sort(mylist,k):
    if len(mylist)<=k:
        return insertion_sort(mylist)
    mid=len(mylist)//2
    left_sort=hybrid_sort(mylist[:mid],k)
    right_sort=hybrid_sort(mylist[mid:],k)
    return merge(left_sort,right_sort)


def print_running_time(n,k):
    my_list=random_list(n)

    start1=time.time()
    for i in range(100):
        current_list=list(my_list)
        merge_sort(current_list)
    end1=time.time()
    print('merge sort running seconds:', end1-start1)



    start2=time.time()
    for i in range(100):
        current_list=list(my_list)
        insertion_sort(current_list)
    end2=time.time()
    print('insertion sort running seconds:', end2-start2)

    start3=time.time()
    for i in range(100):
        current_list=list(my_list)
        hybrid_sort(current_list,k)
    end3=time.time()
    print('hybrid sort running seconds:', end3-start3, 'with k =', k)


def return_running_time_mih(n,k):
    running_time3,running_time1,running_time2=[],[],[]
    my_list=random_list(n)

    
    for i in range(10):
        start1=time.time()
        current_list=list(my_list)
        merge_sort(current_list)
        end1=time.time()
        running_time1.append(end1 - start1)
    # print('merge sort running seconds:', end1-start1)



    for i in range(10):
        start2=time.time()
        current_list=list(my_list)
        insertion_sort(current_list)
        end2=time.time()
        running_time2.append(end2 - start2)
    # print('insertion sort running seconds:', end2-start2)

    for i in range(10):
        start3=time.time()
        current_list=list(my_list)
        hybrid_sort(current_list,k)
        end3=time.time()
        running_time3.append(end3 - start3)
    running_time1.sort()
    running_time2.sort()
    running_time3.sort()
    # print('hybrid sort running seconds:', end3-start3)
    return (running_time1[5], running_time2[5], running_time3[5])


def return_running_time_hybrid(n,k):
    running_time3=[]
    my_list=random_list(n)

    for i in range(10):
        start3=time.time()
        current_list=list(my_list)
        hybrid_sort(current_list,k)
        end3=time.time()
        running_time3.append(end3 - start3)
    running_time3.sort()
    return running_time3[5]


# x_list,y_list,z_list,index=[],[],[],[]
# for i in range(100):
#     x,y,z=return_running_time_mih(i)
#     x_list.append(x)
#     y_list.append(y)
#     z_list.append(z)
#     index.append(i)
# plt.plot(index,x_list,label='merge sort')
# plt.plot(index,y_list,label='insertion sort')
# plt.plot(index,z_list,label='hybrid sort')
# plt.xlabel('list size')
# plt.ylabel('seconds')
# plt.title('Merge Sort vs Insertion Sort vs Hybrid Sort(100 times each)')
# plt.legend()
# plt.show()

# print_running_time(1000, 50)
# print_running_time(1000, 55)
# print_running_time(1000, 60)
# print_running_time(1000, 65)
# print_running_time(1000, 70)

