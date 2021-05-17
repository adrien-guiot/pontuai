class Board:

    def __init__(self, bridges, pawns):
        self.size = 5
        self.pawns = pawns
        self.bridges = bridges

    def printboard(self):
        for y in range(self.size):
            line = ''
            interline = ''
            for x in range(self.size):
                if [x, y] in self.pawns[0]:
                    line += '0'
                elif [x, y] in self.pawns[1]:
                    line += '1'
                else:
                    line += 'X'
                if x < self.size - 1 and (x, y, x + 1, y) in self.bridges:
                    line += '-'
                else:
                    line += ' '
                if y < self.size - 1 and (x, y, x, y + 1) in self.bridges:
                    interline += '|'
                else:
                    interline += ' '
                if x < self.size - 1:
                    interline += ' '
            print(line)
            print(interline)

    def isPawnEliminated(self, pawn):
        (xp, yp) = pawn.split(pawn)
        if xp > 0 and (0, yp, xp, yp) in self.bridges:
            return False
        if yp > 0 and (xp, 0, xp, yp) in self.bridges:
            return False
        if xp < self.size - 1 and (xp, yp, xp + 1, yp) in self.bridges:
            return False
        if yp < self.size - 1 and (xp, yp, xp, yp + 1) in self.bridges:
            return False
        return True

    def isPlayerEliminated(self, player):
        for pawn in self.pawns[player]:
            if self.isPawnEliminated(pawn) is False:
                return False
        return True

    def isEmpty(self, x, y):
        if [x, y] not in self.pawns[0] and [x, y] not in self.pawns[1]:
            return True
        return False

    def listPawnMoves(self, pawn):
        xp = pawn[0]
        yp = pawn[1]
        moves = []
        if yp > 0 and self.isEmpty(xp, yp - 1) and (xp, yp - 1, xp, yp) in self.bridges:
            moves.append((xp, yp, xp, yp - 1))
        if xp < self.size - 1 and self.isEmpty(xp + 1, yp) and (xp, yp, xp + 1, yp) in self.bridges:
            moves.append((xp, yp, xp + 1, yp))
        if yp < self.size - 1 and self.isEmpty(xp, yp + 1) and (xp, yp, xp, yp + 1) in self.bridges:
            moves.append((xp, yp, xp, yp + 1))
        if xp > 0 and self.isEmpty(xp - 1, yp) and (xp - 1, yp, xp, yp) in self.bridges:
            moves.append((xp, yp, xp - 1, yp))
        return moves

    def listPlayersMoves(self):
        moves = [[], []]
        for pawn in self.pawns[0]:
            moves[0].extend(self.listPawnMoves(pawn))
        for pawn in self.pawns[1]:
            moves[1].extend(self.listPawnMoves(pawn))
        return moves

    def findBestMove(self):
        playersMoves = self.listPlayersMoves()
        movesScores = {}
        if len(playersMoves) == 0:
            return None
        for move in playersMoves[0]:
            newpawns = self.pawns[0].copy()
            newpawns.remove([move[0], move[1]])
            newpawns.append([move[2], move[3]])
            newBoard = Board(self.bridges, [newpawns, self.pawns[1]])
            newMoves = newBoard.listPlayersMoves()
            score = len(newMoves[0]) + (12 - len(newMoves[1]))
            movesScores[move] = score
        if len(movesScores) == 0:
             return None
        return max(movesScores, key=movesScores.get)

    def removeBestBridge(self):
        bridgeScores = {}
        for bridge in self.bridges:
            newBridges = self.bridges.copy()
            newBridges.remove(bridge)
            newBoard = Board(newBridges, self.pawns)
            newMoves = newBoard.listPlayersMoves()
            score = len(newMoves[0]) + (12 - len(newMoves[1]))
            bridgeScores[bridge] = score
        return max(bridgeScores, key=bridgeScores.get)
