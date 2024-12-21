class TicTac:
    def __init__(self):   
        self.board = ["-"] * 9
        self.currentplayer = "X"
        self.winner = None
        self.gameRunning = True

    def displayBoard(self):
        print(self.board[0] + " " +  '|' + " " +  self.board[1] + " " + '|' + self.board[2])
        print("---------")
        print(self.board[3] + " " +  '|' + " " +  self.board[4] + " " + '|' + self.board[5])
        print("---------")
        print(self.board[6] + " " +  '|' + " " +  self.board[7] + " " + '|' + self.board[8])

    def playerInput(self):
        try:    
            self.inp = int(input(f"Player {self.currentplayer} Enter a number 1-9: "))
            if self.inp >= 1 and self.inp <= 9 and self.board[self.inp - 1] == "-":
                self.board[self.inp - 1] = self.currentplayer
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

    def switchPlayer(self):
        self.currentplayer = "O" if self.currentplayer == "X" else "X"

    def checkWinner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "-":
                self.winner = self.board[condition[0]]
                return True
        return False

    def checkTie(self):
        return "-" not in self.board

    def playGame(self):
        while self.gameRunning:
            self.displayBoard()
            self.playerInput()
            if self.checkWinner():
                self.displayBoard()
                print(f"Player {self.winner} wins!")
                self.gameRunning = False
            elif self.checkTie():
                self.displayBoard()
                print("It's a tie!")
                self.gameRunning = False
            else:
                self.switchPlayer()


if __name__ == '__main__':
    game = TicTac()
    game.playGame()
