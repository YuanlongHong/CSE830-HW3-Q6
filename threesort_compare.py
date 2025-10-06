import main
import matplotlib.pyplot as plt

x_list,y_list,z_list,index=[],[],[],[]
for i in range(100):
    x,y,z=main.return_running_time_mih(i,k=23)
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)
    index.append(i)
plt.plot(index,x_list,label='merge sort')
plt.plot(index,y_list,label='insertion sort')
plt.plot(index,z_list,label='hybrid sort')
plt.xlabel('list size')
plt.ylabel('seconds')
plt.title('Merge Sort vs Insertion Sort vs Hybrid Sort(100 times each)')
plt.legend()
plt.show()