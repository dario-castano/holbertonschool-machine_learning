#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

people = ('Farrah', 'Fred', 'Felicia')
fruits = ('apples', 'bananas', 'oranges', 'peaches')
range_people = range(len(people))

apple_color = '#ff0000'
banana_color = '#ffff00'
orange_color = '#ff8000'
peach_color = '#ffe5b4'

apple_data = fruit[0, :]
banana_data = fruit[1, :]
orange_data = fruit[2, :]
peach_data = fruit[3, :]

apple_plot = plt.bar(range_people,
                     apple_data,
                     0.5,
                     color=apple_color)

banana_plot = plt.bar(range_people,
                      banana_data,
                      0.5,
                      color=banana_color,
                      bottom=apple_data)

orange_plot = plt.bar(range_people,
                      orange_data,
                      0.5,
                      color=orange_color,
                      bottom=apple_data+banana_data)

peach_plot = plt.bar(range_people,
                     peach_data,
                     0.5,
                     color=peach_color,
                     bottom=apple_data+banana_data+orange_data)

legend_data = (
    apple_plot[0],
    banana_plot[0],
    orange_plot[0],
    peach_plot[0]
)

plt.title('Number of Fruit per Person')
plt.xticks(range_people, people)
plt.yticks(np.arange(0, 81, 10))
plt.ylabel('Quantity of Fruit')
plt.legend(legend_data, fruits)

plt.show()
