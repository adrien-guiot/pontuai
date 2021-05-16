from flask import Flask, request, jsonify

from ..game.board import Board

app = Flask(__name__)


@app.route('/AI', methods=['GET', 'POST'])
def play():
    content = request.json
    bridges = []
    for bridge in content['bridges']:
        bridges.append(tuple(bridge))
    board = Board(bridges, content['pawns'])

    bestMove = board.findBestMove()
    newpawns = content['pawns'][0].copy()
    newpawns.remove([bestMove[0], bestMove[1]])
    newpawns.append([bestMove[2], bestMove[3]])
    newBoard = Board(bridges, [newpawns, content['pawns'][1]])
    bestBridge = newBoard.removeBestBridge()

    board.printboard()
    return jsonify(
        {
            "pawn": bestMove,
            "bridge": bestBridge
        }
    )
