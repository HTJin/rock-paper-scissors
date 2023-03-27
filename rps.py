from random import randint

def generatePlay():
    randomNum = randint(0, 3)

    if randomNum == 0:
        return "Rock"
    elif randomNum == 1:
        return "Paper"
    else:
        return "Scissors"

def choosePlayer(player_name, playersDict, score = 0, combo = 0, w_streak = 0, l_streak = 0):
    playersDict.update({player_name: {'score': score, 'combo': combo, 'w_streak': w_streak, 'l_streak': l_streak}})
    return playersDict

def determineRank(score):
    rank = 'Newbie'
    if score == 0: return rank
    elif 0 < score <= 5: rank = 'Bronze'
    elif 5 < score <= 10: rank = 'Silver'
    elif 10 < score <= 15: rank = 'Gold'
    elif 15 < score <= 20: rank = 'Platinum'
    elif 20 < score <= 25: rank = 'Diamond'
    elif 25 < score <= 30: rank = 'Master'
    elif 30 < score <= 35: rank = 'Grandmaster'
    elif score > 35: rank = 'G O A T'
    elif 0 > score >= -5: rank = 'Egg'
    elif -5 > score >= -10: rank = 'Unlucky'
    elif -10 > score >= -15: rank = 'Loser'
    elif -15 > score >= -20: rank = 'Weenie'
    elif -20 > score >= -25: rank = 'Super Weenie'
    elif -25 > score >= -30: rank = 'Mega Weenie Loser'
    elif -30 > score >= -35: rank = 'Hardstuck Loser'
    elif score < -35: rank = 'Trash'
    return rank
        
def link(score):
    if score == 0: return "Enter the link" 
    elif score <= 5: 
        return input(
            "Enter the link:https://www.vectorstock.com/royalty-free-vector/bronze-medal-with-number-three-icon-cartoon-style-vector-14203473")
    elif score <= 10:
        return input(
            "Enter the link:https://pixabay.com/illustrations/medal-silver-award-competition-1622529/")
    elif score <= 15:
        return input(
            "Enter the link:https://www.dreamstime.com/royalty-free-stock-images-little-girl-golden-medal-thumb-up-image13280539")
    elif score <= 20:
        return input(
            "Enter the link:https://pokemonromhack.com/wp-content/uploads/2014/06/Pokemon_Light_Platinum_BoxArt.png")
    elif score <= 25:
        return input(
            "Enter the link:https://www.nativeskatestore.co.uk/accessories-c3/skateboard-stickers-c15/dgk-dgk-x-diamond-skateboard-sticker-p10165")
    elif score <= 30:
        return input(
            "Enter the link:https://en.wikipedia.org/wiki/MasterChef_(American_season_12)#/media/File:MCS12poster.jpg")
    elif score <= 35: 
        return input(
            "Enter the link:https://twitter.com/GrandMOogway")
    elif score > 35:
        return input(
            "Enter the link:http://1.bp.blogspot.com/-XdRtST5NkrM/T7z433dfS9I/AAAAAAAAGFs/A7Agez6HAxs/s1600/mountain_goat.jpg")
    
    elif score >= -5:
        return input(
            "Enter the link:https://www.photos-elsoar.com/wp-content/images/Egg-Picture-A.jpg")
    elif score >= -10:
        return input(
            "Enter the link:https://www.underscores.fr/wp-content/uploads/2019/07/Unlucky-Charms-Cover.jpg")
    elif score >= -15:
        return input(
            "Enter the link:https://external-preview.redd.it/OZGPYpQASrrhEJVKGMHbtKYsL5lS6Vpn1WG2gD_1UFc.jpg?auto=webp&v=enabled&s=8a6c28faa60b9fd35c4fec1bf5fa0a34a70a35b4")
    elif score >= -20:
        return input(
            "Enter the link:https://www.sbmania.net/locations.php?id=96")
    elif score >= -25:
        return input(
            "Enter the link:https://spongebob.fandom.com/wiki/Super_Weenie_Hut_Jr's?file=SuperWeenieHutJrsStock.png")
    elif score >= -30:
        return input(
            "Enter the link:https://spongebob.fandom.com/wiki/Weenie_Hut_General?file=No_Weenies_Allowed_200.png")
    elif score >= -35:
        return input(
            "Enter the link:https://external-preview.redd.it/OZGPYpQASrrhEJVKGMHbtKYsL5lS6Vpn1WG2gD_1UFc.jpg?auto=webp&v=enabled&s=8a6c28faa60b9fd35c4fec1bf5fa0a34a70a35b4")
    elif score < -35:
        return input(
            "Enter the link:https://biogossipy.com/playboi-carti-bio-age-affair-songs-model-net-worth-height/")


def playGame():
    moves = ['rock', 'r', 'paper', 'p', 'scissors', 's', 'rank', 'score', 'create', 'switch', 'i quit', 'players']
    players = {}
    user_name = input(prLPurpleNone("What is your name? "))
    players = choosePlayer(user_name, players)
    score, combo, w_streak, l_streak = 0, 0, 0, 0

    print(f'\nWelcome Player {prPinkNone(user_name)}!')
    rank = determineRank(0)
    print(f'Looks like your rank is: {prOrangeNone(rank)}, with a score of {prBlueNone(score)}')
    
    while True:
        cpu_move = generatePlay()
        player_move = input(prLPurpleNone(f"\nThrow your move [{prGreenNone('Rock')}{prLPurpleNone('/')}{prGreenNone('Paper')}{prLPurpleNone('/')}{prGreenNone('Scissors')}{prLPurpleNone(' or ')}{prGreenNone('r')}{prLPurpleNone('/')}{prGreenNone('p')}{prLPurpleNone('/')}{prGreenNone('s')}{prLPurpleNone('], ')}{prGreenNone('rank/score')}{prLPurpleNone(', ')}{prGreenNone('create')}{prLPurpleNone(', ')}{prGreenNone('switch')}{prLPurpleNone(', or ')}{prLPurpleNone('type')} {prRedNone('I quit')}{prLPurpleNone(':')} ")).strip().lower()
        
        if player_move not in moves:
            prLCyan('Player input not recognized, please try again.')
        
        elif player_move == 'players':
            print(players)
        
        elif player_move == 'create':
            players = choosePlayer(user_name, players, score, combo, w_streak, l_streak)
            while True:
                prGreen('You chose to create a new player\n')
                user_name = input(prLPurpleNone("What is your new player name? "))
                if user_name not in players.keys():
                    print(f'\nWelcome Player {prPinkNone(user_name)}!')
                    print(f"Looks like your rank is: {prOrangeNone('Newbie')}, with a score of {prBlueNone(0)}")
                    players = choosePlayer(user_name, players)
                    score, combo, w_streak, l_streak = 0, 0, 0, 0
                    break
                else:
                    print(f'\n{prPinkNone(user_name)} was already found in the list of players.')
                    overwrite = input(f"Would you like to overwrite and reset {prPinkNone(user_name)} (y/n)? ").strip().lower()
                    if overwrite == 'y':
                        print(f'\nWelcome Player {prPinkNone(user_name)}!')
                        print(f"Looks like your rank is: {prOrangeNone('Newbie')}, with a score of {prBlueNone(0)}")
                        players = choosePlayer(user_name, players)
                        score, combo, w_streak, l_streak = 0, 0, 0, 0
                        break
                    elif overwrite == 'n':
                        print(f"You've chosen to not overwrite {prPinkNone(user_name)}. Please input another name to create.\n")
                    else:
                        prLCyan('Input not recognized, please try again.')

        elif player_move == 'switch':
            while True:
                if len(players) > 1:
                    prGreen('Switching to another player\n')
                else:
                    prYellow('There are no other users to switch to.')
                    break
                players = choosePlayer(user_name, players, score, combo, w_streak, l_streak)
                switch_name = input("Player name you wish to switch to? ")
                if switch_name not in players.keys():
                    print(f'Player {prPinkNone(switch_name)} was not found as a player. Try again.\n')
                else:
                    print(f'Switching over to Player "{prPinkNone(switch_name)}"!\n')
                    user_name = switch_name
                    players = choosePlayer(user_name, players, players[user_name]['score'], players[user_name]['combo'], players[user_name]['w_streak'], players[user_name]['l_streak'])
                    print(f'Welcome back Player {prPinkNone(user_name)}!')
                    rank = determineRank(players[user_name]['score'])
                    print(f"\n{prPinkNone(user_name)}'s rank is: {prOrangeNone(rank)}, with a score of {prBlueNone(players[user_name]['score'])}")
                    print(f"You left the game with your combo at {prCyanNone(players[user_name]['combo'])}, with a win streak of {prGreenNone(players[user_name]['w_streak'])} round(s), and a loss streak of {prRedNone(abs(players[user_name]['l_streak']))} round(s)")
                    break
        
        elif player_move == 'rank' or player_move == 'score':
            rank = determineRank(players[user_name]['score'])
            print(f"\n{prPinkNone(user_name)}'s rank is: {prOrangeNone(rank)}, with a score of {prBlueNone(players[user_name]['score'])}")
            link(players[user_name]["score"])
        
        elif player_move == 'i quit':
            prYellow('\nThank you for playing\n')
            prRedBg('[ -- DAILY HIGHSCORES -- ]')
            place = 1
            for player, item in sorted(players.items(), key=lambda x: x[1]['score'], reverse=True):
                print(f"{prCyanNone(place)}. {prPinkNone(player)} ---------- Score: {prBlueNone(item['score'])}, Win streak: {prGreenNone(item['w_streak'])}, Loss streak: {prRedNone(abs(item['l_streak']))}, Rank: {prOrangeNone(determineRank(item['score']))}")
                place += 1
            break
        
        elif player_move == 'rock' or player_move == 'r':
            prPurple(f'The computer played: {prPinkNone(cpu_move)}')
            if cpu_move == 'Rock':
                prYellow('Game Tied')
            elif cpu_move == "Paper":
                if combo > 1: prCyan('** COMBO BREAK **')
                if combo > 0: combo = 0
                else: combo -= 1
                if combo < l_streak: l_streak = combo
                score -= 5
                players = choosePlayer(user_name, players, score+combo, combo, w_streak, l_streak)
                prRed('You Lose')
            elif cpu_move == "Scissors":
                if combo < 0: combo = 0
                else: combo += 1
                if combo > 1 : prCyan(f'COMBO BONUS ==> +{combo}')
                if combo > w_streak: w_streak = combo
                score += 5
                players = choosePlayer(user_name, players, score+combo, combo, w_streak, l_streak)
                prGreen('You Win')
        
        elif player_move == 'paper' or player_move == 'p':
            prPurple(f'The computer played: {prPinkNone(cpu_move)}')
            if cpu_move == 'Rock':
                if combo < 0: combo = 0
                else: combo += 1
                if combo > 1 : prCyan(f'COMBO BONUS ==> +{combo}')
                if combo > w_streak: w_streak = combo
                score += 5
                players = choosePlayer(user_name, players, score+combo, combo, w_streak, l_streak)
                prGreen('You Win')
            elif cpu_move == "Paper":
                prYellow('Game Tied')
            elif cpu_move == "Scissors":
                if combo > 1: print('** COMBO BREAK **')
                if combo > 0: combo = 0
                else: combo -= 1
                if combo < l_streak: l_streak = combo
                score -= 5
                players = choosePlayer(user_name, players, score+combo, combo, w_streak, l_streak)
                prRed('You Lose')
        
        elif player_move == 'scissors' or player_move == 's':
            prPurple(f'The computer played: {prPinkNone(cpu_move)}')
            if cpu_move == 'Rock':
                if combo > 1: prCyan('** COMBO BREAK **')
                if combo > 0: combo = 0
                else: combo -= 1
                if combo < l_streak: l_streak = combo
                score -= 5
                players = choosePlayer(user_name, players, score+combo, combo, w_streak, l_streak)
                prRed('You Lose')
            elif cpu_move == "Paper":
                if combo < 0: combo = 0
                else: combo += 1
                if combo > 1 : prCyan(f'COMBO BONUS ==> +{combo}')
                if combo > w_streak: w_streak = combo
                score += 5
                players = choosePlayer(user_name, players, score+combo, combo, w_streak, l_streak)
                prGreen('You Win')
            elif cpu_move == "Scissors":
                prYellow('Game Tied')

def prRed(skk): return print("\033[31m{}\033[00m".format(skk))
def prRedNone(skk): return "\033[31m{}\033[00m".format(skk)
def prGreen(skk): return print("\033[32m{}\033[00m".format(skk))
def prGreenNone(skk): return "\033[32m{}\033[00m".format(skk)
def prOrangeNone(skk): return "\033[33m{}\033[00m".format(skk)
def prBlueNone(skk): return "\033[34m{}\033[00m".format(skk)
def prPurple(skk): return print("\033[35m{}\033[00m".format(skk))
def prCyan(skk): return print("\033[36m{}\033[00m".format(skk))
def prCyanNone(skk): return "\033[36m{}\033[00m".format(skk)
def prYellow(skk): return print("\033[93m{}\033[00m".format(skk))
def prLPurpleNone(skk): return "\033[94m{}\033[00m".format(skk)
def prPinkNone(skk): return "\033[95m{}\033[00m".format(skk)
def prLCyan(skk): return print("\033[96m{}\033[00m".format(skk))
def prRedBg(skk): return print("\033[41m{}\033[00m".format(skk))

playGame()