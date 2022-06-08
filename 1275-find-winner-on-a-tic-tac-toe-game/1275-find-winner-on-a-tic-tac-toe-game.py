class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        score = [0]*8
        for i, (L,R) in enumerate(moves):
            if i % 2 == 0:
                # A's move 
                x = 1
            else:
                x = -1
            
            score[L] += x
            score[R+3] += x
            
            if L == R:
                score[6] += x
            if L + R == 2:
                score[7] += x
            
        for i in score:
            if i == 3:
                return 'A'
            elif i == -3:
                return 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'
            
        
