class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        for i in asteroids:
            if mass >= i:
                mass += i
            else:
                return False
        return True
