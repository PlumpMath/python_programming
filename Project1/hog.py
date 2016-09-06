"""The Game of Hog"""

from dice import four_sided_dice, six_sided_dice, make_test_dice
from ucb import main, trace, log_current_line, interact

goal = 100          # The goal of Hog is to score 100 points.
commentary = True  # Whether to display commentary for every roll.

# Taking turns

def roll_dice(num_rolls, dice=six_sided_dice, who='Boss Hogg'):
    """Calculate WHO's turn score after rolling DICE for NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A function of no args and returns an integer outcome.
    who:        Name of the current player, for commentary.
    """
    score = 0
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    for i in range(0, num_rolls):
        outcome = dice()
        if commentary:
            announce(outcome, who)
        if(outcome == 1):
            """ Any of the dice come up a 1 (Pig out), 
            in which case she scores only 1 point for the turn
            """
            score = 1
            break
        else:
            """ She scores the sum of the dice outcomes """
            score += outcome
        
    return score

def take_turn(num_rolls, opponent_score, dice=six_sided_dice, who='Boss Hogg'):
    """Simulate a turn in which WHO chooses to roll NUM_ROLLS, perhaps 0.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args and returns an integer outcome.
    who:             Name of the current player, for commentary.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    if commentary:
        print(who, 'is going to roll', num_rolls, 'dice')
    if(num_rolls == 0):
        """ opponent score will be between [0,99], because 100 is winning score """
        return ((opponent_score//10) + 1)
    else:
        return roll_dice(num_rolls, dice, who)
        

def take_turn_test():
    """Test the roll_dice and take_turn functions using test dice."""
    print('-- Testing roll_dice with deterministic test dice --')
    print('In mohet01 take_turn_test()', __name__)
    
    dice = make_test_dice(4, 6, 1)
    assert roll_dice(2, dice) == 10, 'First two rolls total 10'
    
    dice = make_test_dice(5, 6, 1)
    assert roll_dice(2, dice) == 11, 'First two rolls total 11'
    
    dice = make_test_dice(3, 6, 1)
    assert roll_dice(2, dice) == 9, 'First two rolls total 9'
    
    dice = make_test_dice(4, 6, 1)
    assert roll_dice(3, dice) == 1, 'Third roll is a 1'

    dice = make_test_dice(1, 2, 3)
    assert roll_dice(3, dice) == 1, 'First roll is a 1'

    dice = make_test_dice(3, 2, 1)
    assert roll_dice(2, dice) == 5, 'First two rolls is a 5'
    
    print('-- Testing take_turn --')
    dice = make_test_dice(4, 6, 1)
    assert take_turn(2, 0, dice) == 10, 'First two rolls total 10'

    dice = make_test_dice(4, 6, 1)
    assert take_turn(3, 20, dice) == 1, 'Third roll is a 1'

    assert take_turn(0, 34) == 4, 'Opponent score 10s digit is 3'
    assert take_turn(0, 71) == 8, 'Opponent score 10s digit is 7'
    assert take_turn(0,  7) == 1, 'Opponont score 10s digit is 0'

    '*** You may add more tests here if you wish ***'

    print('Tests for roll_dice and take_turn passed.')


    # Commentator

def announce(outcome, who):
    """Print a description of WHO rolling OUTCOME."""
    print(who, 'rolled a', outcome)
    print(draw_number(outcome))

def draw_number(n, dot='*'):
    """Return a text representation of rolling the number N.
    If a number has multiple possible representations (such as 2 and 3), any
    valid representation is acceptable.

    >>> print(draw_number(5))
     -------
    | *   * |
    |   *   |
    | *   * |
     -------

    >>> print(draw_number(6, '$'))
     -------
    | $   $ |
    | $   $ |
    | $   $ |
     -------
    """
    if n == 1:
        #str = '     -------\n' + '    |       |\n' + '    |   ' + dot + '   |\n' + '    |       |\n' + '     -------\n' 
        str = draw_dice(True, False, False, False, dot)
    elif n == 2:
        #str = '     -------\n' + '    |       |\n' + '    | ' + dot + '   ' + dot + ' |\n' + '    |       |\n' + '     -------\n'
        str = draw_dice(False, False, False, True, dot)
    elif n == 3:
        #str = '     -------\n' + '    |       |\n' + '    | ' + dot + ' ' + dot + ' ' + dot + ' |\n' + '    |       |\n' + '     -------\n'
        str = draw_dice(True, False, False, True, dot)
    elif n == 4:
        #str = '     -------\n' + '    | ' + dot + '   ' + dot + ' |\n' + '    |       |\n' + '    | ' + dot + '   ' + dot + ' |\n' + '     -------\n'
        str = draw_dice(False, True, True, False, dot)
    elif n == 5:
        #str = '     -------\n' + '    | ' + dot + '   ' + dot + ' |\n' + '    |   ' + dot + '   |\n' + '    | ' + dot + '   ' + dot + ' |\n' + '     -------\n'
        str = draw_dice(True, True, True, False, dot)
    elif n == 6:
        #str = '     -------\n' + '    | ' + dot + '   ' + dot + ' |\n' + '    | ' + dot + '   ' + dot + ' |\n' + '    | ' + dot + '   ' + dot + ' |\n' + '     -------\n'
        str = draw_dice(False, True, True, True, dot)
    else:
        str = 'Invalid number n'
    return str


def draw_dice(c, f, b, s, dot):
    """Return an ASCII art representation of a die roll.

    c, f, b, & s are boolean arguments. This function returns a multi-line
    string of the following form, where the letters in the diagram are either
    filled if the corresponding argument is true, or empty if it is false.

     -------
    | b   f |
    | s c s |
    | f   b |
     -------

    The sides with 2 and 3 dots have 2 possible depictions due to rotation.
    Either representation is acceptable.

    This function uses Python syntax not yet covered in the course.

    c, f, b, s -- booleans; whether to place dots in corresponding positions.
    dot        -- A length-one string to use for a dot.
    """
    assert len(dot) == 1, 'Dot must be a single symbol'
    border = ' -------'
    def draw(b):
        return dot if b else ' '
    c, f, b, s = map(draw, [c, f, b, s])
    top = ' '.join(['|', b, ' ', f, '|'])
    middle = ' '.join(['|', s, c, s, '|'])
    bottom = ' '.join(['|', f, ' ', b, '|'])
    return '\n'.join([border, top, middle, bottom, border])

    
def num_allowed_dice(score, opponent_score):
    """Return the maximum number of dice allowed this turn. The maximum
    number of dice allowed is 10 unless the sum of SCORE and
    OPPONENT_SCORE has a 7 as its ones digit.

    >>> num_allowed_dice(1, 0)
    10
    >>> num_allowed_dice(5, 7)
    10
    >>> num_allowed_dice(7, 10)
    1
    >>> num_allowed_dice(3, 24)
    1
    """
    if ((score + opponent_score)%10) == 7:
        return 1
    else:
        return 10
    

def select_dice(score, opponent_score):
    """Select 6-sided dice unless the sum of scores is a multiple of 7.

    >>> select_dice(4, 24) == four_sided_dice
    True
    >>> select_dice(16, 64) == six_sided_dice
    True
    """
    if ((score + opponent_score)%7) == 0:
        return four_sided_dice
    else:
        return six_sided_dice

def play(strategy0, strategy1):
    """Simulate a game and return 0 if the first player wins and 1 otherwise.

    A strategy function takes two scores for the current and opposing players.
    It returns the number of dice that the current player will roll this turn.

    If a strategy returns more than the maximum allowed dice for a turn, then
    the maximum allowed is rolled instead.

    strategy0:  The strategy function for player 0, who plays first.
    strategy1:  The strategy function for player 1, who plays second.
    """
    who = 0         # Which player is about to take a turn, 0 (first) or 1 (second)
    score0 = 0      # Score of player0
    score1 = 0      # Score of player1
    while True:
        if who:
            num_of_dice = strategy1(score1, score0)
            opponent_score = score0
            type_of_dice = select_dice(score1, score0)
        else:
            num_of_dice = strategy0(score0, score1)
            type_of_dice = select_dice(score0, score1)
            opponent_score = score1    
        player_name = name(who)
        score = take_turn(num_of_dice, opponent_score, type_of_dice, player_name)
        if who:
            score1 += score
            if score1 >= goal:
                break
            else:
                who = 1- who
        else:
            score0 += score
            if score0 >= goal:
                break
            else:
                who = 1 - who
    return who
    

def name(who):
    """Return the name of player WHO, for player numbered 0 or 1."""
    if who == 0:
        return 'Player 0'
    elif who == 1:
        return 'Player 1'
    else:
        return 'An unknown player'
        
@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--take_turn_test', '-t', action='store_true')
    parser.add_argument('--play_interactively', '-p', action='store_true')
    parser.add_argument('--play_basic', '-b', action='store_true')
    parser.add_argument('--run_experiments', '-r', action='store_true')
    parser.add_argument('--final_strategy_test', '-f', action='store_true')
    args = parser.parse_args()
    for name, execute in args.__dict__.items():
        if execute:
            globals()[name]()