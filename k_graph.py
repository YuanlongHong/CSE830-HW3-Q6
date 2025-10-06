import main
import matplotlib.pyplot as plt


x,y=[],[]
for i in range(2, 101):
    y.append(main.return_running_time_hybrid(1000,i))
    x.append(i)


print(min(y), 'seconds when k =', y.index(min(y))+2)
plt.plot(x,y)
plt.xlabel('k value')
plt.ylabel('seconds')
plt.title('Hybrid Sort with different k value(1000 elements, 100 times each)')
plt.show()