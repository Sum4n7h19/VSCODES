# Write a program to generate mean, median, mode, stdev using statistics module.

import statistics as st
data = [1, 3, 5, 7, 11, 9, 11, 13]

# Calculating average
print(st.mean(data))
# Checking centerd value in a sorted list
print(st.median(data))
# Checking repeadted value
print(st.mode(data))
# Calculating standard deviation
print(st.stdev(data))

