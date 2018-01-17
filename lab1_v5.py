# !/usr/bin/python3
# Lynnae Griffiths
# Copyright (c) 2018 Lynnae Griffiths
# except sections attributed to Bart Massey
# see https://github.com/BartMassey/movie-jobs

# New Beginnings, Winter 2018
# Lab 1, Algorithms 

# NOTE:
# Version 5, without Prof. Massey's visualizer 

# Movie Jobs problem, from Chapter 1 of Skiena's 
# 'Algorithm Design Manual'
# Program accepts an integer (number of jobs), 
# randomly generates a schedule of job durations,
# and picks a schedule that maximizes the number of 
# non-overlapping jobs. 

# To run, include filename, and the number of jobs to schedule, n.
# 'python3 <filename> n'

from random import randrange
from sys import argv, stdin

# The following code is attributed to Prof. Bart Massey:
# subsets() and subsets() functions.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def subsets(s):
	"Return a list of all subsets of a given set s."

	t = [set()]
	for e in s:
		v = list(t)
		for w in t:
			v.append({e} | w)
		t = v
	return t

def geninst(n):
    "Generate an instance of size n."

    intervals = []
    for _ in range(n):
        width = randrange(1, n)
        start = randrange(4 * n - width)
        end = start + width
        intervals.append((start, end))
    return intervals
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def has_overlaps(S):
	"Return true if any intervals in the given subset overlap. Intervals are (start, end) tuples"
	for i in S:
		for j in S:
			if i == j:
				continue
			if overlap(i,j):
				return True
	return False	

def overlap(i, j):
	"Take in two tuples, i and j, that represent (start, end) intervals, and compare for overlap. Return true if they overlap."
	if i[0] >= j[0] and i[0] < j[1]:
		return True
	if j[0] >= i[0] and j[0] < i[1]:
		return True
	return False 

# Generate and display an instance.
if __name__ == "__main__":
    n = int(argv[1])
    inst = geninst(n)
    for i in inst:
        print(*i)

def movie_jobs(I):
	Jmax = set()
	for J in I:
		if len(J) <= len(Jmax):
			continue
		if has_overlaps(J):
			continue
		Jmax = J
	return Jmax

# main sequence

# ~~~~~~~~~~~~~~~~~~~~~INTERACTIVE VERSION (DISABLED)~~~~~~~~~~~~~~~~~
# print('MOVIE JOBS SCHEDULER')
# n = input('How many jobs would you like to schedule?\n')

# get user input 
# n = int(n)

# generate random schedule
# schedule = geninst(n)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# generate all possible subsets of given schedules
n_subsets = subsets(inst)

# identify best schedule, maximizing number of non-overlapping jobs
soln = movie_jobs(n_subsets)


print("subsets of {} jobs".format(n))
for i in inst:
	print(*i)
print("best set:", soln)
	
