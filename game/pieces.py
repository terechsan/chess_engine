from player import Player


class Piece:
    def __init__(self, x, y, player: Player):
        self.x = x
        self.y = y
        self.player = player

    def calculate_moves(self, board):
        return [], []

    def __repr__(self):
        return f"Type: {type(self)} Player: {self.player.name}"


class Pawn(Piece):
    def __init__(self, x, y, player: Player):
        super(Pawn, self).__init__(x, y, player)
        self.has_moved = False

    def calculate_moves(self, board):
        moves = []
        attacks = []
        if self.player is Player.WHITE:
            direction = 1
        else:
            direction = -1
        moves.append((self.x, self.y + direction))
        if not self.has_moved:
            moves.append((self.x, self.y + 2*direction))
        moves_filtered = []
        for move in moves:
            if board[move] is None:
                moves_filtered.append(move)
            else:
                moves = moves_filtered
                del moves_filtered
                break
        attacks.append((self.x + 1, self.y + direction))
        attacks.append((self.x - 1, self.y + direction))
        attacks_filtered = []
        for attack in attacks:
            if isinstance(board[move], Piece):
                attacks_filtered.append(attack)
        attacks = attacks_filtered
        del attacks_filtered
        return moves, attacks

