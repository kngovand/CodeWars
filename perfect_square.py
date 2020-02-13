import math

def find_next_square(sq):
    rooted = math.sqrt(sq)
    if rooted.is_integer():
        rooted+=1
        next_sq = rooted * rooted
        return next_sq
    else:
        return -1