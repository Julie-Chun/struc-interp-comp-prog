"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    new = [paragraphs[x] for x in range(len(paragraphs)) if select(paragraphs[x])]
    if len(new)-1 < k :
        return ''
    else:
        return new[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    

    def helper(par):
        par = par.lower()
        new = ''
        lis = []
        for k in range(len(par)):
            if par[k] in alph:
                new += par[k]

        prev = 0
        for q in range(len(new)):
            if new[q] == ' ':
                print("DEBUG: ",q)
                lis += [new[prev:q]]
                prev = q+1
            if q == len(new)-1:
                lis += [new[prev:q+1]]

        print("DEBUG:",lis,new)
        for i in range(len(topic)):
            for j in range(len(lis)):
                if topic[i] == lis[j]:
                    return True
        return False

    return helper

    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if typed == '' or reference == '':
        return 0.0


    total = len(typed_words)
    points = 0

    for i in range(len(typed_words)):
        if i == len(reference_words):
            return (points/total)*100

        if typed_words[i] == reference_words[i]:
            points += 1

    return (points/total)*100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    if typed == '':
        return 0.0
    else:
        length = len(list(typed))/5
        time = 60/elapsed
        return length*time
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    lowest = diff_function(user_word, valid_words[0], limit)
    index = 0
    for i in range(len(valid_words)):
        diff = diff_function(user_word, valid_words[i], limit)
        if lowest > diff:
            lowest = diff
            index = i

    if user_word in valid_words:
        return user_word
    elif lowest > limit:
        return user_word
    else:
        return valid_words[index]
    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

    s = len(start)
    g = len(goal)

    if limit < 0:
        return limit +1
    elif s == 0 or g == 0:
        return s + g
    elif start[0] != goal[0]:
        return 1 + sphinx_swap(start[1::], goal[1::], limit-1)
    else:
        return sphinx_swap(start[1::], goal[1::], limit)

    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if limit < 0: # Fill in the condition
        # BEGIN
        return max(len(start), len(goal)) #or return 1
        # END

    if len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        return max(len(start), len(goal))
        # END

    else:
        add_diff = goal[0] + start # Fill in these lines
        remove_diff = start[1::]
        substitute_diff = goal[0] + start[1::]
        # BEGIN
        
        if start[0] != goal[0]:
            return 1 + min(feline_fixes(add_diff[1::], goal[1::], limit-1), feline_fixes(remove_diff, goal, limit-1),feline_fixes(substitute_diff[1::], goal[1::], limit-1))
            
        elif start[0] == goal[0]: 
            return feline_fixes(start[1::],goal[1::],limit)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    total = len(prompt)
    correct = 0

    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            print("DEBUG: MATCH", typed[i],)
            correct += 1
        else:
            break

    result = correct/total

    send({'id': id, 'progress': result})
    return result
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    times = []

    for x in range(len(times_per_player)):
        times += [[]]
        for i in range(1,len(times_per_player[x])):
            times[x] += [times_per_player[x][i]-times_per_player[x][i-1]]

    return game(words,times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    result = []
    for p in players:
        result += [[]]
    
    for w in words:
        index = 0
        Min = time(game, 0, w)
        for p in players:
            if time(game,p,w) < Min:
                Min = time(game,p,w)
                index = p
        result[index] += [word_at(game, w)]

    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)