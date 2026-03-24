import matplotlib.pyplot as plt
import numpy as np

plt.ion() 
fig, ax = plt.subplots()

for i in range(10): 
    
  
    data = [np.random.normal(loc=0, scale=1, size=100)]
    

    ax.boxplot(data)
    
    ax.set_title(f"Dynamic Box Plot (Update {i+1})")
    
    plt.pause(1) 

plt.ioff()
plt.show()