#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig, axs = plt.subplots(3, 2)
gridspec = axs[2, 0].get_gridspec()
axs[2, 0].remove()
axs[2, 1].remove()

fig.suptitle('All in One')
fig.set_size_inches(7.0, 7.0)
plt.subplots_adjust(wspace=0.35, hspace=0.9)

red_plot = axs[0, 0]
magenta_scatter = axs[0, 1]
blue_decay = axs[1, 0]
two_plots = axs[1, 1]
big_histogram = fig.add_subplot(gridspec[2, :])

red_plot.plot(y0, color='red')
red_plot.set_xlim(0, 10)

magenta_scatter.scatter(x1, y1, s=2, color='m')
magenta_scatter.set_title('Men\'s Height vs Weight', fontsize='x-small')
magenta_scatter.set_xlabel('Height (in)', fontsize='x-small')
magenta_scatter.set_ylabel('Weight (lbs)', fontsize='x-small')

blue_decay.plot(x2, y2)
blue_decay.set_title('Exponential Decay of C-14', fontsize='x-small')
blue_decay.set_xlabel('Time (years)', fontsize='x-small')
blue_decay.set_ylabel('Fraction Remaining', fontsize='x-small')
blue_decay.set_yscale('log')
blue_decay.set_xlim(0, 28650)

two_plots.plot(x3, y31, color='red', linestyle='--', label='C-14')
two_plots.plot(x3, y32, color='green', linestyle='-', label='Ra-226')
two_plots.set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
two_plots.set_xlabel('Time (years)', fontsize='x-small')
two_plots.set_ylabel('Fraction Remaining', fontsize='x-small')
two_plots.set_xlim(0, 20000)
two_plots.set_ylim(0, 1)
two_plots.legend(fontsize='x-small')

big_histogram.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
big_histogram.set_title("Project A", fontsize='x-small')
big_histogram.set_xlabel("Grades", fontsize='x-small')
big_histogram.set_ylabel("Number of Students", fontsize='x-small')
big_histogram.set_xlim(0, 100)
big_histogram.set_ylim(0, 30)
big_histogram.set_xticks(np.arange(0, 101, step=10))
