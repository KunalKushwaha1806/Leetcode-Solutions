class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_remove = 10
        alice_turn = True
        while n > 0:
            if stones_remove > n:
                return not alice_turn
            n -= stones_remove
            stones_remove -= 1
            alice_turn = not alice_turn
        return not alice_turn