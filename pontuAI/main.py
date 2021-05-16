from game.board import Board

if __name__ == '__main__':
    pawns = [[
        [1, 1],
        [2, 1],
        [3, 1]
    ], [
        [1, 3],
        [2, 3],
        [3, 3]
    ]]

    bridges = []
    for y in range(5):
        for x in range(5):
            if x < 4:
                bridges.append((x, y, x + 1, y))
            if y < 4:
                bridges.append((x, y, x, y + 1))

    b = Board(bridges, pawns)

    bestMove = b.findBestMove()
    newpawns = pawns[0].copy()
    newpawns.remove([bestMove[0], bestMove[1]])
    newpawns.append([bestMove[2], bestMove[3]])
    newBoard = Board(bridges, [newpawns, pawns[1]])
    bestBridge = newBoard.removeBestBridge()

    newBridges = bridges.copy()
    newBridges.remove(bestBridge)
    newBoard = Board(newBridges, [newpawns, pawns[1]])
    newBoard.printboard()
