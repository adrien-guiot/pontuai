from flask import Flask, request, jsonify

from ..game.board import Board

app = Flask(__name__)


@app.route('/ai', methods=['POST', 'OPTIONS'])
def play():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return '', 204, headers

    content = request.json
    bridges = []
    for bridge in content['bridges']:
        bridges.append(tuple(bridge))
    board = Board(bridges, content['pawns'])

    bestMove = board.findBestMove()
    if bestMove is not None:
        newpawns = content['pawns'][0].copy()
        newpawns.remove([bestMove[0], bestMove[1]])
        newpawns.append([bestMove[2], bestMove[3]])
    else:
        newpawns = content['pawns'][0]
    newBoard = Board(bridges, [newpawns, content['pawns'][1]])
    bestBridge = newBoard.removeBestBridge()

    newBoard.printboard()
    response = jsonify(
        {
            "pawn": bestMove,
            "bridge": bestBridge
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
