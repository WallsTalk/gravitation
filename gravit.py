
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:23:03 2022

@author: PC
"""

from matplotlib import pyplot as plt
from math import sin, cos, degrees, atan2, hypot, radians
from numpy import subtract, divide, multiply, array

#import matplotlib.animation as ani
from time import sleep



def make_plot(xy, color):
    # list of cordinates
    x, y = [g/10e9 for g in xy]
    # Plotting
    plt.plot(x,y, color)
    # Displaying plot
    

def vector(cord1, cord2):
    return subtract(cord2, cord1)


def euclidean_distance(vector):
    return hypot(*vector)


def calculate_angle(cord1, cord2):
    # find lengths of x and y and then put the lengths to atan2 function
    x, y = vector(cord1, cord2)
    #print(x, y)
    # above the angle is 0 left is clockwise is 180dgr, while counter is -180 
    rad_angle = atan2(x, y)
    #angle = degrees(rad_angle)    
    return rad_angle



def calculate_gravity(cord1, cord2, m1, m2):
    # F = G*(m1*m2)/r**2
    G = 6.674e-11 # m3⋅kg−1⋅s−2
    r = euclidean_distance(vector(cord1, cord2))
    #print(r)
    gravity = G*(m1*m2)/(r**2)
    return gravity
    
    
def calculate_acceleration(F, m):
    return F/m

def sum_vectors(v1, v2):
    return tuple( array(v1) + array(v2) )



# ert = {
#     'm': 1, # kg
#     'xy': (0, 5), # m
#     'v': 1e-6, # m/s initial velocity perependicular to the gravity
    
#     }
# sun = {
#     'm': 100, # kg
#     'xy': (0,0), #m
#     'v': 1, # m/s
#        }
ert = {
    'm': 5.972e24, # kg
    'xy': (0,147095e6), # m at perhelion, 152100e6 perihelion
    'v': 30.29e3,#e3, # m/s  29.29 at aphelion initial velocity perependicular to the gravity
    'color': 'bo'
    }
sun = {
    'm': 1.989e30, # kg
    'xy': (0,0), #m
    'v': 30.29e3, # m/s
    'color': 'yo',
       }

# =============================================================================
# Let v=(x1,y1)−(x0,y0). Normalize this to u=v/||v||.
# 
# The point along your line at a distance d from (x0,y0) is then (x0,y0)+du, 
# if you want it in the direction of (x1,y1), or (x0,y0)−du, 
# if you want it in the opposite direction. One advantage of doing the calculation this way 
# is that you won't run into a problem with division by zero in the case that x0=x1.
# =============================================================================


count = 0
day = 86400 # in seconds
step = day # time to make progress in graphic
g_velocity = (21.2e3, -21.2e3)
earth_trajectory = []
while True:
    # print(ert['xy'])
    
    # calculate angle
    #nx, ny = ert['xy']
    #angle = calculate_angle(ert['xy'], sun['xy'])
    # calculate_current move
    # ancient_movement = ( nx - ert['v']*cos(angle), ny + ert['v']*cos(angle) )
    # ert['xy'] = ancient_movement #sum_vectors(ancient_movement, g_velocity)


    
    #this is where we calculate (gravity_vector for upcoming moves)
    g = calculate_gravity(ert['xy'], sun['xy'], ert['m'], sun['m'])
    a = calculate_acceleration(g, ert['m'])

    v_ert2sun = vector( ert['xy'], sun['xy'] )
    eu_dist = euclidean_distance(v_ert2sun)
    # normalized vector is  portion that planet will pass in 1 iteration
    norm_vector_unit = divide(v_ert2sun, eu_dist)

    g_velocity = sum_vectors(g_velocity, norm_vector_unit*a)
    ert['xy'] = sum_vectors(ert['xy'], g_velocity )

 
    
    
    
    


    
    if count%step == 0:
        print(ert['xy'])
        print(g_velocity)
        print()
        earth_trajectory.append(ert['xy'])
        for g in earth_trajectory:
            make_plot(g, color='bo')
        make_plot(sun['xy'], color='yo')
        plt.plot()
        plt.axis([-20, 20, -20, 20])
        plt.grid()
        plt.gca().set_aspect("equal")
        plt.title("day:{}, dist:{} Mm".format(int(count/day), round(eu_dist/1000000)))
        plt.show()
    count += 1
# =============================================================================
# =============================================================================
# (0, 147095000000.0)
# (0, 0) 3.141592653589793
# (30290.0, 147094969710.0)
# 
# (30290.0, 147094969710.0)
# (-2.0592138575314003e-07, -0.9999999999999788) -3.1415924476684074
# (60579.999999793436, 147094939419.0)
# 
# (60579.999999793436, 147094939419.0)
# (-6.177642420680411e-07, -1.9999999999998939) -3.141592241746937
# (90869.9999991731, 147094909127.0)
# =============================================================================
# =============================================================================
# (0, 147090000000.0)
# (0, 0) 3.141592653589793 180.0
# (30290.0, 147089969710.0)
# 
# (30290.0, 147089969710.0)
# (-2.0592838559773036e-07, -0.9999999999999788) -3.1415924476614077 -179.99998820117264
# (60579.99999979343, 147089939419.0)
# 
# (60579.99999979343, 147089939419.0)
# (-6.17785241607578e-07, -1.9999999999998939) -3.1415922417329374 -179.9999764023404
# (90869.99999917307, 147089909127.0)
# =============================================================================