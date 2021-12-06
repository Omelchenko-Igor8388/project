import matplotlib.pyplot as plt

potato_price = [0.67,0.8,2.05,59.83]
cabbage_price = [0.44,0.66,2.24,61]
onion_price = [0.54,0.71,2.13,51]
tomatoes_price = [0.68,0.84,4.50,30]
cucumbers_price = [0.86,1.2,4.50,25]
apple_price = [1,1.30,5.75,70]
year = [2007,2008,2011,2017]

plt.plot(year,potato_price,label = "Картопля")
plt.plot(year,cabbage_price,label = "Капуста")
plt.plot(year,onion_price,label = "Цибуля")
plt.plot(year,tomatoes_price,label = "Помідори")
plt.plot(year,cucumbers_price,label = "Огірки")
plt.plot(year,apple_price,label = "Яблука")
plt.xlabel("Рік")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

plt.show()