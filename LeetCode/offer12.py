# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:08:51 2021

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以
从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过
了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符
串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格
子之后，路径不能再次进入这个格子。

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
 
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

@author: qzh
"""

"""
遍历点，然后DFS
"""

class Solution:
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    flag = False
    def exist(self, board, word):
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    self.search(board, i, j, word, 1)
                    if self.flag: return True
                    board[i][j] = word[0]
        return False
    
    def search(self, board, start_x, start_y, word, pointer):
        if pointer == len(word):
            self.flag = True
            return
        for i in range(4):
            x, y = start_x + self.d[i][0], start_y + self.d[i][1]
            if x >= 0 and y >= 0 and x < len(board) and y < len(board[0]):
                if board[x][y] == word[pointer]:
                    board[x][y] = ''
                    self.search(board, x, y, word, pointer + 1)
                    if self.flag: return
                    board[x][y] = word[pointer]
                
solution = Solution()
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = 'AAB'
print(solution.exist(board, word))