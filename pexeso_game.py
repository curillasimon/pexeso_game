import random
import math

class PexesoGame:
    def __init__(self, size):
        if size % 2 != 0:
            raise ValueError('Number of cards must be odd!')
        self.size = size
        self.revealed = []
        self.board = self._generate_board()
    
    # 1 function -> from my 3 functions
    def _generate_board(self):
        count = self.size
        half = count // 2
        numbers = random.sample(range(1, 100), half)
        full_numbers = numbers * 2
        random.shuffle(full_numbers)

        side = int(math.sqrt(count))

        board = []
        for i in range(0, len(full_numbers), side):
            row = []
            for j in range(i, i+side):
                row.append(full_numbers[j])
            board.append(row)
        
        return board
    
    def is_revealed(self, x, y):
        return (x,y) in self.revealed
    
    def guess_pair(self, x1, y1, x2, y2):
        if (x1,y1) == (x2,y2):
            return False, "Zvolil si rovnaké políčko."
        if self.is_revealed(x1, y1) or self.is_revealed(x2, y2):
            return False, "Jedna z pozícií je už odhalená."
        
        value1 = self.board[x1][y1]
        value2 = self.board[x2][y2]

        if value1 == value2:
            self.revealed.extend([(x1, y1), (x2, y2)])
            return True, "✅ Našiel si pár!"
        else:
            return False, "❌ Nesprávny pár."
        
    def get_board_view(self, reveal_temp=[]):
        view = []
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[0])):
                if (i,j) in self.revealed or (i,j) in reveal_temp:
                    row.append(f"{self.board[i][j]:>2}")
                else:
                    row.append(" #")
            view.append(" ".join(row))

        return "\n".join(view)
    
    
    def is_complete(self):
        return len(self.revealed) == self.size
    
if __name__ == "__main__":
    size = int(input("Zadaj pocet kariet (napr. 36): "))
    game = PexesoGame(size)

    print("Hra začína!")
    print(game.get_board_view())

    while not game.is_complete():
        # Prvý výber
        x1 = int(input("Suradnica[][y1]: "))
        y1 = int(input("Suradnica[x1][]: "))
        while game.is_revealed(x1,y1):
            print("Táto pozícia je už odhalená.")
            x1 = int(input("Znova y1: "))
            y1 = int(input("Znova x1: "))

        print("* Odhalené 1. číslo:")
        print(game.get_board_view(reveal_temp=[(x1,y1)]))

        # Druhy výber
        x2 = int(input("Suradnica[][y2]: "))
        y2 = int(input("Suradnica[x2][]: "))
        while game.is_revealed(x2,y2):
            print("Táto pozícia je už odhalená.")
            x2 = int(input("Znova y1: "))
            y2 = int(input("Znova x1: "))

        print("* Odhalené 2. číslo:")
        print(game.get_board_view(reveal_temp=[(x2,y2)]))

        match, message = game.guess_pair(x1, y1, x2, y2)
        print(message)
        print("-------------")
        print("Odhalené pozície:")
        print(game.revealed)
        print("-------------")
        print(game.get_board_view())

    print("🎉 Hra dokončená! 🎉")

        
        
