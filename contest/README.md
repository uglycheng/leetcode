# LeetCode Solutions
These are solutions for some leetcode contest problems written in Python. Problems are from [LeetCode China](https://leetcode-cn.com/problems/two-sum).

## 5379.Stone Game III
<br>Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
<br>Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.
<br>The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.
<br>The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.
<br>Assume Alice and Bob play optimally
<br>Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.
<br>**Constraints:**

* 1 <= values.length <= 50000
* -1000 <= values[i] <= 1000

<br>Solution Code: [5379_stone_game_3.py](./5379_stone_game_3.py)