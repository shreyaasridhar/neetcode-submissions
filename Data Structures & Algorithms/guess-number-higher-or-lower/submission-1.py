# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        myGuess = n // 2
        l = 0
        r = n
        while (l <= r):
            if guess(myGuess) == 0:
                return myGuess
            if guess(myGuess) == 1:
                l = myGuess + 1
            else:
                r = myGuess - 1
            myGuess = (r - l) // 2 + l
        
        return myGuess