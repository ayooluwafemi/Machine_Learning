# Machine Learning is making the computer learn from studying data and statistics.
# Machine Learning is a step into the direction of artificial intelligence (AI).
# Machine Learning is a program that analyses data and learns to predict the outcome.
import numpy
from scipy import stats
import matplotlib.pyplot as plt

# Mean value is the average value
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

# Median value is the value in the middle, after you have sorted all the values
x = numpy.median(speed)
print(x)

# Mode value is the value that appears the most number of times
x = stats.mode(speed)
print(x)

# Standard Deviation: describes how spread out the values are
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

# Variance
# Variance is another number that indicates how spread out the values are.
# if you take the square root of the variance, you get the standard deviation!
# Or if you multiply the standard deviation by itself, you get the variance!
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)

# Percentiles: What is the 75. percentile? 
# The answer is 43, meaning that 75% of the people are 43 or younger
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)

# What is the age that 90% of the people are younger than?
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 90)
print(x)

# Data Distribution: Create an array containing 250 random floats between 0 and 5:
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

# We use the array from the example above to draw a histogram with 5 bars
# 52 values are between 0 and 1
# 48 values are between 1 and 2
# 49 values are between 2 and 3
# 51 values are between 3 and 4
# 50 values are between 4 and 5
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()

x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

# We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
# We specify that the mean value is 5.0, and the standard deviation is 1.0.
# Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
# And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

# Machine Learning - Scatter Plot
# Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
# The first array will have the mean set to 5.0 with a standard deviation of 1.0.
# The second array will have the mean set to 10.0 with a standard deviation of 2.0:
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()

# Linear Regression
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)
def myfunc(x):
  return slope * x + intercept
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Polynomial Regression
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# R-Squared
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print(r2_score(y, mymodel(x)))



















