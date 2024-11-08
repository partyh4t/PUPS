
# chess board validator

chess_board =  {'1a': 'wrook','2a': 'wbishop','9z': 'znight','4a': 'wqueen','5a': 'wpawn','6a': 'wbishop','7a': 'wknight','8a': 'wqueen','2h': 'wrook','1b': 'wbishop','2b': 'wknight','3b': 'wqueen'}


def isValidChessBoard(board):
    keys = board.keys()
    values = board.values()
    pawn_count = 0
    queen_count = 0
    king_count = 0
    w_count = 0
    b_count = 0
    if len(board) > 32:
        print('Too many peices!')
    for i, j in keys:
        if int(i) > 8 or j > 'h':
            print('The peice on ' + i + j + ' is not a valid position!')
    for k in values:
        if k[0] not in ('w', 'b') or k[1:] not in ('bishop', 'rook', 'pawn', 'knight', 'queen', 'king'):
            print(k + ' is not a valid piece!')
        if k[0] == 'w':
            w_count += 1
        elif k[0] == 'b':
            b_count += 1
        if k[1:] == 'pawn':
            pawn_count += 1
        if k[1:] == 'king':
            king_count += 1
        if k[1:] == 'queen':
            queen_count += 1
    if pawn_count > 8 or queen_count > 1 or king_count > 1:
        print('Too many pawns, queens, or kings!')
    if w_count > 16:
        print('Too many white pieces!')
    if b_count > 16:
        print('Too many black pieces!')
    

isValidChessBoard(chess_board)
