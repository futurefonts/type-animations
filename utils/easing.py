import math 

def easeInOutQuad(t, b, c, d):
    # t is the current time (or position) of the tween.
    # b is the beginning value.
    # c is the change between the beginning and destination value
    # d is the total time of the tween.
    t /= d/2
    if t < 1:
        return c/2*t*t + b
    t-=1
    return -c/2 * (t*(t-2) - 1) + b

def easeInQuad(t, b, c, d):
    t /= d
    return c*t*t + b
	
def easeOutQuad(t, b, c, d):
    t /= d
    return c * (1 - (1 - t) * (1 - t)) + b;



def easeInOutQuart(t, b, c, d):
    t /= d/2
    if t < 1:
        return c/2*t*t*t*t + b
    t -= 2
    return -c/2 * (t*t*t*t - 2) + b

def easeInQuart(t, b, c, d):
    t /= d
    return c*t*t*t*t + b

def easeOutQuart(t, b, c, d):
    t /= d
    return c * ((t-1)*(t-1)*(t-1)*(1-t)+1) + b


def easeInOutExp(t, b, c, d):
    #t /= d/2
    t /= d

    if t == 0 or t == 1:
        return t

    if t < 0.5:
        return 0.5 * math.pow(2, (20 * t) - 10)

    return -0.5 * math.pow(2, (-20 * t) + 10) + 1

def easeInExp(t, b, c, d):
    t /= d
    if t == 0:
        return 0
    return c * (math.pow(2, 10 * (t - 1))) + b

def easeOutExp(t, b, c, d):
    t /= d
    if t == 1:
        return 1
    return c * (1 - math.pow(2, -10 * t)) + b
    
# y = easeInExp(9,0,1,10)
# print(y)