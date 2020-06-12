from gui.board import *
from gui.algorithm import Algorithm

def main():
    algorithm = Algorithm()
    print(board.getSquares(board.pieceSet(RED, KING)))
    print(board.legalMoves(PAWN, board.square(4, 1), RED))

if __name__ == '__main__':
    main()
