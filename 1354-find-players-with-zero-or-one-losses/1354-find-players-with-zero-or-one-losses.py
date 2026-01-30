class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = {}
        for winner, loser in matches:
            if winner not in losses_count:
                losses_count[winner] = 0
            
            if loser not in losses_count:
                losses_count[loser] = 0
            
            losses_count[loser] += 1
        no_losses = []
        one_loss = []
        for player, count in losses_count.items():
            if count == 0:
                no_losses.append(player)
            elif count == 1:
                one_loss.append(player)
        
        return [sorted(no_losses), sorted(one_loss)]