# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)

# Your grader will use this function to help them verify your code
def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  

#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,		              #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################



def z_score(x, mu, sigma):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """
    
    # Braxton Allen
    # Patricia Krause
    
    # Your code goes between this comment and the return
    numerator = x - mu
    result = numerator / sigma

    return result

print(z_score(1, 51.94, 28.25424657))
print(z_score(3, 51.94, 28.25424657))
print(z_score(4, 51.94, 28.25424657))
print(z_score(12, 51.94, 28.25424657))
print(z_score(14, 51.94, 28.25424657))
print(z_score(14, 51.94, 28.25424657))
print(z_score(19, 51.94, 28.25424657))
print(z_score(19, 51.94, 28.25424657))
print(z_score(19, 51.94, 28.25424657))
print(z_score(21, 51.94, 28.25424657))
print(z_score(25, 51.94, 28.25424657))
print(z_score(28, 51.94, 28.25424657))
print(z_score(29, 51.94, 28.25424657))
print(z_score(29, 51.94, 28.25424657))
print(z_score(30, 51.94, 28.25424657))
print(z_score(33, 51.94, 28.25424657))
print(z_score(37, 51.94, 28.25424657))
print(z_score(42, 51.94, 28.25424657))
print(z_score(44, 51.94, 28.25424657))
print(z_score(44, 51.94, 28.25424657))
print(z_score(45, 51.94, 28.25424657))
print(z_score(46, 51.94, 28.25424657))
print(z_score(49, 51.94, 28.25424657))
print(z_score(53, 51.94, 28.25424657))
print(z_score(53, 51.94, 28.25424657))
print(z_score(54, 51.94, 28.25424657))
print(z_score(55, 51.94, 28.25424657))
print(z_score(57, 51.94, 28.25424657))
print(z_score(58, 51.94, 28.25424657))
print(z_score(59, 51.94, 28.25424657))
print(z_score(61, 51.94, 28.25424657))
print(z_score(62, 51.94, 28.25424657))
print(z_score(64, 51.94, 28.25424657))
print(z_score(65, 51.94, 28.25424657))
print(z_score(66, 51.94, 28.25424657))
print(z_score(68, 51.94, 28.25424657))
print(z_score(68, 51.94, 28.25424657))
print(z_score(75, 51.94, 28.25424657))
print(z_score(75, 51.94, 28.25424657))
print(z_score(76, 51.94, 28.25424657))
print(z_score(82, 51.94, 28.25424657))
print(z_score(86, 51.94, 28.25424657))
print(z_score(87, 51.94, 28.25424657))
print(z_score(88, 51.94, 28.25424657))
print(z_score(94, 51.94, 28.25424657))
print(z_score(96, 51.94, 28.25424657))
print(z_score(96, 51.94, 28.25424657))
print(z_score(97, 51.94, 28.25424657))
print(z_score(97, 51.94, 28.25424657))
print(z_score(98, 51.94, 28.25424657))
print(z_score(51.94, 51.94, 28.25424657))
print(z_score(60, 51.94, 28.25424657))




print(z_score(-25, -0.5, 14.57737974))
print(z_score(-24, -0.5, 14.57737974))
print(z_score(-23, -0.5, 14.57737974))
print(z_score(-22, -0.5, 14.57737974))
print(z_score(-21, -0.5, 14.57737974))
print(z_score(-20, -0.5, 14.57737974))
print(z_score(-19, -0.5, 14.57737974))
print(z_score(-18, -0.5, 14.57737974))
print(z_score(-17, -0.5, 14.57737974))
print(z_score(-16, -0.5, 14.57737974))
print(z_score(-15, -0.5, 14.57737974))
print(z_score(-14, -0.5, 14.57737974))
print(z_score(-13, -0.5, 14.57737974))
print(z_score(-12, -0.5, 14.57737974))
print(z_score(-11, -0.5, 14.57737974))
print(z_score(-10, -0.5, 14.57737974))
print(z_score(-9, -0.5, 14.57737974))
print(z_score(-8, -0.5, 14.57737974))
print(z_score(-7, -0.5, 14.57737974))
print(z_score(-6, -0.5, 14.57737974))
print(z_score(-5, -0.5, 14.57737974))
print(z_score(-4, -0.5, 14.57737974))
print(z_score(-3, -0.5, 14.57737974))
print(z_score(-2, -0.5, 14.57737974))
print(z_score(-1, -0.5, 14.57737974))
print(z_score(0, -0.5, 14.57737974))
print(z_score(24, -0.5, 14.57737974))
print(z_score(23, -0.5, 14.57737974))
print(z_score(22, -0.5, 14.57737974))
print(z_score(21, -0.5, 14.57737974))
print(z_score(20, -0.5, 14.57737974))
print(z_score(19, -0.5, 14.57737974))
print(z_score(18, -0.5, 14.57737974))
print(z_score(17, -0.5, 14.57737974))
print(z_score(16, -0.5, 14.57737974))
print(z_score(15, -0.5, 14.57737974))
print(z_score(14, -0.5, 14.57737974))
print(z_score(13, -0.5, 14.57737974))
print(z_score(12, -0.5, 14.57737974))
print(z_score(11, -0.5, 14.57737974))
print(z_score(10, -0.5, 14.57737974))
print(z_score(9, -0.5, 14.57737974))
print(z_score(8, -0.5, 14.57737974))
print(z_score(7, -0.5, 14.57737974))
print(z_score(6, -0.5, 14.57737974))
print(z_score(5, -0.5, 14.57737974))
print(z_score(4, -0.5, 14.57737974))
print(z_score(3, -0.5, 14.57737974))
print(z_score(2, -0.5, 14.57737974))
print(z_score(1, -0.5, 14.57737974))
print(z_score(-0.5, -0.5, 14.57737974))
print(z_score(25, -0.5, 14.57737974))




print(z_score(0, 337.5, 205.649378))
print(z_score(25, 337.5, 205.649378))
print(z_score(50, 337.5, 205.649378))
print(z_score(75, 337.5, 205.649378))
print(z_score(100, 337.5, 205.649378))
print(z_score(125, 337.5, 205.649378))
print(z_score(150, 337.5, 205.649378))
print(z_score(175, 337.5, 205.649378))
print(z_score(200, 337.5, 205.649378))
print(z_score(225, 337.5, 205.649378))
print(z_score(250, 337.5, 205.649378))
print(z_score(275, 337.5, 205.649378))
print(z_score(300, 337.5, 205.649378))
print(z_score(325, 337.5, 205.649378))
print(z_score(350, 337.5, 205.649378))
print(z_score(375, 337.5, 205.649378))
print(z_score(400, 337.5, 205.649378))
print(z_score(425, 337.5, 205.649378))
print(z_score(450, 337.5, 205.649378))
print(z_score(475, 337.5, 205.649378))
print(z_score(500, 337.5, 205.649378))
print(z_score(525, 337.5, 205.649378))
print(z_score(550, 337.5, 205.649378))
print(z_score(575, 337.5, 205.649378))
print(z_score(600, 337.5, 205.649378))
print(z_score(625, 337.5, 205.649378))
print(z_score(650, 337.5, 205.649378))
print(z_score(675, 337.5, 205.649378))
print(z_score(337.5, 337.5, 205.649378))
print(z_score(460, 337.5, 205.649378))
