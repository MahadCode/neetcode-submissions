class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for asteroid in asteroids:
            if asteroid > 0:
                stk.append(asteroid)
            else:
                while stk and stk[-1] > 0 and -(asteroid) > stk[-1]:
                    stk.pop()
                
                if stk:
                    if stk[-1] < 0:
                        stk.append(asteroid)
                    elif stk[-1] + asteroid == 0:
                        stk.pop()
                else:
                    stk.append(asteroid)
                        
            
        return stk
        