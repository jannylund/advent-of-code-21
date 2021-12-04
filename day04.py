from utils.time import get_time, start_timer


def get_drawn(game):
    return [int(number) for number in game[0].split(",")]


# generate multi-dimenisonal arrays of the games with a tuple of (value, hit)
def get_games(game):
    game = game[1:]
    games = dict()
    curr_game = -1
    for line in game:
        if not line:
            curr_game = curr_game + 1
            games[curr_game] = []
        else:
            games[curr_game].append([(int(number), 0) for number in line.split(" ") if number])
    return games


def play(games, drawn):
    rows = len(games[0])
    cols = len(games[0][0])
    for num in drawn:
        for i in range(len(games)):
            for row in range(rows):
                for col in range(cols):
                    value, hit = games[i][row][col]
                    if value == num:
                        games[i][row][col] = (value, 1)
            if is_winner(games[i]):
                return games[i], num
    return None


def play_loosing(games, drawn):
    rows = len(games[0])
    cols = len(games[0][0])
    for num in drawn:
        for i in range(len(games)):
            if games[i]:
                for row in range(rows):
                    for col in range(cols):
                        value, hit = games[i][row][col]
                        if value == num:
                            games[i][row][col] = (value, 1)
                if is_winner(games[i]):
                    game_length = len([game for game in range(len(games)) if games[game] != None])
                    if game_length > 1:
                        games[i] = None
                    else:
                        return games[i], num
    return None


def is_winner(game):
    rows = len(game)
    cols = len(game[0])

    # check rows first.
    for row in range(rows):
        row_score = 0
        for col in range(cols):
            value, hit = game[row][col]
            row_score = row_score + hit
        if row_score == cols:
            return True

    # and then check cols.
    for col in range(cols):
        col_score = 0
        for row in range(rows):
            value, hit = game[row][col]
            col_score = col_score + hit
        if col_score == cols:
            return True
    return False


def get_unmarked_sum(game):
    rows = len(game)
    cols = len(game[0])
    unmarked_sum = 0
    for row in range(rows):
        for col in range(cols):
            value, hit = game[row][col]
            if hit == 0:
                unmarked_sum = unmarked_sum + value
    return unmarked_sum


if __name__ == "__main__":
    with open("input/day04.txt") as f:
        game = f.read().splitlines()

    drawn = get_drawn(game)
    games = get_games(game)

    start = start_timer()
    winning_game, winning_num = play(games, drawn)
    final_score = get_unmarked_sum(winning_game) * winning_num
    print("result day 04 part 1: winning_score={} in {} ms".format(final_score, get_time(start)))

    start = start_timer()
    loosing_game, loosing_num = play_loosing(games, drawn)
    final_score = get_unmarked_sum(loosing_game) * loosing_num
    print("result day 04 part 2: loosing_score={} in {} ms".format(final_score, get_time(start)))
