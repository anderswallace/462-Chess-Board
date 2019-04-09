import chess
import chess.engine

# This program acts as the AI that the user will play against

# The move is set as a string from one space to another, i.e. "e5e6"
# To quit the game, user can input 'q'
def user_move(board, engine):
	chess_move = input("User Move: ")
	if chess_move == "q":
		engine.quit()
		print("\nQUITTING GAME")
		quit()
	else:
		player_move = chess.Move.from_uci(chess_move)
		board.push(player_move)
	
	return

def main():
	engine = chess.engine.SimpleEngine.popen_uci("/Users/anderswallace/Documents/Documents/School/CSCE_462/462-Chess-Board/stockfish-10-64")
	board = chess.Board()

	print("----- GAME START -----\n")

	while not board.is_game_over():
		result = engine.play(board, chess.engine.Limit(time=0.100))
		board.push(result.move)
		print("AI Move\n")
		print(board)
		print(" ")
		user_move(board, engine)
	engine.quit()

main()


