#I want to go up a flight of stairs that has n steps. I can either take 1 or 2 steps each
#time. How many different ways can I go up this flight of stairs? Write a function
#count_stair_ways that solves this problem for me.

def count_stair_ways(n):
    if n == 1: # 1 way to flight
        return 1
    if n == 2: # 2 ways to flight
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)