def passthepillow(self, n, time):
    return n - abs((n - 1) - (time % (2 * (n - 1))))
