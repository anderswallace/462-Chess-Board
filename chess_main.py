import chess
import chess.engine

# This program acts as the AI that the user will play against

# The move is set as a string from one space to another, i.e. "e5e6"
# To quit the game, user can input 'q'
def user_move(user_text, board):
	
	player_move = chess.Move.from_uci(user_text)
	board.push(player_move)
	print(" ")
	print(board)
	print(" ")
	
	return board

def check_input(user_text, board):
	if user_text == "q":
		engine.quit()
		print("\nQUITTING GAME")
		quit()
	elif user_text == "r":
		print("\nRESTARTING GAME\n")
		new_board = chess.Board()
		return new_board
	else:
		board = user_move(user_text, board)
		return board



def main():
	engine = chess.engine.SimpleEngine.popen_uci("/Users/anderswallace/Documents/Documents/School/CSCE_462/462-Chess-Board/stockfish-10-64")
	board = chess.Board()

	print("----- GAME START -----\n")

	while not board.is_game_over():
		result = engine.play(board, chess.engine.Limit(time=0.500))
		board.push(result.move)
		print("AI Move\n")
		print(board)
		print(" ")
		user_choice = input("User Move: ")
		board = check_input(user_choice, board)

	engine.quit()


main()


