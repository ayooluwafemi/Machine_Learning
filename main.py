# Machine Learning is making the computer learn from studying data and statistics.
# Machine Learning is a step into the direction of artificial intelligence (AI).
# Machine Learning is a program that analyses data and learns to predict the outcome.
import numpy
from scipy import stats

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






















