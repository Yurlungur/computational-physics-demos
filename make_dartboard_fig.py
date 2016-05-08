#!/usr/bin/env python2

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2016-05-08 14:23:55 (jmiller)>

# This program randomly peppers a dartboard with darts, either within
# the inner ring or the outer. The dart placement is random, but the
# darts avoid the green lines. This is mostly a utility to make
# pretty, readable pictures. It should not be used for anything else.

import numpy as np
import scipy as sp
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import misc
import random

board = misc.imread('figures/Dart_Board.PNG')
xmax,ymax = board.shape[:-1]
xcenter,ycenter = xmax/2,ymax/2
r_inner = 500
r_outer = 1000
frame_outname = 'figures/darts-frame-{}.png'

def get_random_point_in_circle(rmin,rmax,center):
    theta = random.uniform(0,2*np.pi)
    r = random.uniform(rmin,rmax)
    p = np.array([r*np.cos(theta),
                  r*np.sin(theta)])
    p += center
    return p

if __name__ == "__main__":
    random.seed()
    npoints = 9
    center = np.array([xcenter,ycenter])
    r_range = [(100,r_inner-100),(r_inner+100,r_outer-200)]
    points = [np.empty((npoints,2),
                       dtype='float64')\
              for r in r_range]
    for i in range(npoints):
        for j,(rmin,rmax) in enumerate(r_range):
            points[j][i,...] = get_random_point_in_circle(rmin,rmax,center)

    plt.imshow(board)
    plt.xlim(0,xmax)
    plt.ylim(0,ymax)
    
    plt.plot(points[0][0,0],points[0][0,1],'ro')
    plt.savefig(frame_outname.format(0),bbox_inches='tight')
    plt.plot(points[1][0,0],points[1][0,1],'ro')
    plt.savefig(frame_outname.format(1),bbox_inches='tight')
    plt.plot(points[1][:2,0],points[1][:2,1],'ro')
    plt.savefig(frame_outname.format(2),bbox_inches='tight')
    plt.plot(points[1][:3,0],points[1][:3,1],'ro')
    plt.savefig(frame_outname.format(3),bbox_inches='tight')
    plt.plot(points[0][:2,0],points[0][:2,1],'ro')
    plt.savefig(frame_outname.format(4),bbox_inches='tight')
    plt.plot(points[0][:3,0],points[0][:3,1],'ro')
    plt.plot(points[1][...,0],points[1][...,1],'ro')
    plt.savefig(frame_outname.format(5),bbox_inches='tight')
