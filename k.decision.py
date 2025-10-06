import main

results=[]
for i in range(100):
    x,y=[],[]
    for i in range(2, 101):
        y.append(main.return_running_time_hybrid(1000,i))
        x.append(i)
    results.append(y.index(min(y))+2)

results.sort()
k=results[50]
print(k, 'is the best k value')