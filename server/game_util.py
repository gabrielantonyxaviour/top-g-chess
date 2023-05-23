def draw_board(current_board):
    """Draw board

    Keyword arguments:
    current_board -- chess.Board()
    """
    board_img = chess.svg.board(current_board, flipped=ai_white)
    svg2png(bytestring=board_img, write_to="/content/board.png")
    img = cv2.imread("/content/board.png", 1)
    cv2_imshow(img)


def can_checkmate(move, current_board):
    """Return True if a move can checkmate

    Keyword arguments:
    move -- chess.Move
    current_board -- chess.Board()
    """
    fen = current_board.fen()
    future_board = chess.Board(fen)
    future_board.push(move)
    return future_board.is_checkmate()


def ai_play_turn(current_board):
    """Handdle the A.I's turn

    Keyword arguments:
    current_board -- chess.Board()
    """
    clear_output()
    draw_board(current_board)
    print("\n")
    print(
        r"""                                        
                      ._ o o
                      \_`-)|_       Hold on,  
                   ,""       \        Let me think...
                 ,"  ## |   ಠ ಠ.        
               ," ##   ,-\__    `.
             ,"       /     `--._;)
           ,"     ## /
         ,"   ##    /
        """
    )
    for move in current_board.legal_moves:
        if can_checkmate(move, current_board):
            current_board.push(move)
            return

    nb_moves = len(list(current_board.legal_moves))

    if nb_moves > 30:
        current_board.push(minimax_root(4, current_board))
    elif nb_moves > 10 and nb_moves <= 30:
        current_board.push(minimax_root(5, current_board))
    else:
        current_board.push(minimax_root(7, current_board))
    return


def human_play_turn(current_board):
    """Handle the human's turn

    Keyword arguments:
    current_board = chess.Board()
    """
    clear_output()
    draw_board(current_board)
    print("\n")
    print("\n")
    print("number moves: " + str(len(current_board.move_stack)))
    move_uci = input("Enter your move: ")

    try:
        move = chess.Move.from_uci(move_uci)
    except:
        return human_play_turn(current_board)
    if move not in current_board.legal_moves:
        return human_play_turn(current_board)
    current_board.push(move)
    return


def play_game(turn, current_board):
    """Play through the whole game

    Keyword arguments:
    turn -- True for A.I plays first
    current_board -- chess.Board()
    """
    if current_board.is_stalemate():
        clear_output()
        print("Stalemate: both A.I and human win")
        return
    else:
        if not turn:
            if not current_board.is_checkmate():
                human_play_turn(current_board)
                return play_game(not turn, current_board)
            else:
                clear_output()
                draw_board(current_board)
                print("A.I wins")
                return
        else:
            if not current_board.is_checkmate():
                ai_play_turn(current_board)
                return play_game(not turn, current_board)
            else:
                clear_output()
                draw_board(current_board)
                print("Human wins")
                return


def play():
    """Init and start the game"""
    global ai_white
    ai_white = True

    board = chess.Board()
    human_first = input("Care to start? [y/n]: ")
    clear_output()
    if human_first == "y":
        ai_white = False
        return play_game(False, board)
    else:
        return play_game(True, board)
