from random import randint
from io import BytesIO
from urllib.request import urlopen
from PIL import Image, ImageTk
import tkinter as tk

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

def playGame():
    moves = ['rock', 'r', 'paper', 'p', 'scissors', 's', 'rank', 'score', 'create', 'switch', 'i quit', 'players']
    players = {}
    user_name = input(prLPurpleNone("What is your name? "))
    players = choosePlayer(user_name, players)
    score, combo, w_streak, l_streak = 0, 0, 0, 0

    print(f'\nWelcome Player {prPinkNone(user_name)}!')
    rank = determineRank(0)
    print(f'Looks like your rank is: {prOrangeNone(rank)}, with a score of {prBlueNone(score)}')
    imgPop(players[user_name]['score'])

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
                prGreenBg('[ -- SWITCHABLE PLAYERS -- ]')
                prPink('\n'.join(player for player in players.keys()))
                switch_name = input(prLPurpleNone("Player name you wish to switch to? "))
                if switch_name not in players.keys():
                    print(f"Player {prPinkNone(switch_name)} was {prRedNone('not found')} as a player. Try again.\n")
                else:
                    print(f'Switching over to Player "{prPinkNone(switch_name)}"!\n')
                    user_name = switch_name
                    players = choosePlayer(user_name, players, players[user_name]['score'], players[user_name]['combo'], players[user_name]['w_streak'], players[user_name]['l_streak'])
                    print(f'Welcome back Player {prPinkNone(user_name)}!')
                    rank = determineRank(players[user_name]['score'])
                    print(f"\n{prPinkNone(user_name)}'s rank is: {prOrangeNone(rank)}, with a score of {prBlueNone(players[user_name]['score'])}")
                    imgPop(players[user_name]['score'])
                    print(f"You left the game with your combo at {prCyanNone(players[user_name]['combo'])}, with a win streak of {prGreenNone(players[user_name]['w_streak'])} round(s), and a loss streak of {prRedNone(abs(players[user_name]['l_streak']))} round(s)")
                    break
        
        elif player_move == 'rank' or player_move == 'score':
            rank = determineRank(players[user_name]['score'])
            print(f"\n{prPinkNone(user_name)}'s rank is: {prOrangeNone(rank)}, with a score of {prBlueNone(players[user_name]['score'])}")
            imgPop(players[user_name]['score'])

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

def imgPop(score):
    if score == 0: return show_image('https://www.shutterstock.com/image-illustration/newbie-new-employee-member-introduction-260nw-1165795669.jpg') 
    elif 0 < score <= 5: return show_image('https://cdn.vectorstock.com/i/1000x1000/34/73/bronze-medal-with-number-three-icon-cartoon-style-vector-14203473.webp')
    elif 5 < score <= 10: return show_image('https://content.presentermedia.com/files/clipart/00003000/3720/silver_medal_award_second_place_800_wht.jpg')
    elif 10 < score <= 15: return show_image('https://thumbs.dreamstime.com/z/little-girl-golden-medal-thumb-up-13280539.jpg')
    elif 15 < score <= 20: return show_image('https://2.bp.blogspot.com/-PS_V0OKZ9Y4/WRUIbVKaPaI/AAAAAAAAAFo/m2yllJgumwMCrCwGepTGSvBhzJH5KNLUgCLcB/s1600/Pokemon_Light_Platinum_BoxArt.png')
    elif 20 < score <= 25: return show_image('https://www.nativeskatestore.co.uk/images/dgk-dgk-x-diamond-skateboard-sticker-p10165-20666_medium.jpg')
    elif 25 < score <= 30: return show_image('https://upload.wikimedia.org/wikipedia/en/7/72/MCS12poster.jpg')
    elif 30 < score <= 35:  return show_image('https://www.scrolldroll.com/wp-content/uploads/2022/07/quotes-from-Kung-Fu-Panda-7.jpg')
    elif score > 35: return show_image('http://1.bp.blogspot.com/-XdRtST5NkrM/T7z433dfS9I/AAAAAAAAGFs/A7Agez6HAxs/s1600/mountain_goat.jpg')
    elif 0 > score >= -5: return show_image('https://www.photos-elsoar.com/wp-content/images/Egg-Picture-A.jpg')
    elif -5 >  score >= -10: return show_image('https://www.underscores.fr/wp-content/uploads/2019/07/Unlucky-Charms-Cover.jpg')
    elif -10 > score >= -15: return show_image('https://external-preview.redd.it/OZGPYpQASrrhEJVKGMHbtKYsL5lS6Vpn1WG2gD_1UFc.jpg?auto=webp&v=enabled&s=8a6c28faa60b9fd35c4fec1bf5fa0a34a70a35b4')
    elif -15 > score >= -20: return show_image('https://www.sbmania.net/pictures/48a/207.png')
    elif -20 > score >= -25: return show_image('https://static.wikia.nocookie.net/spongebob/images/5/52/SuperWeenieHutJrsStock.png/revision/latest/scale-to-width-down/1000?cb=20221117021328')
    elif -25 > score >= -30: return show_image('https://static.wikia.nocookie.net/spongebob/images/1/19/No_Weenies_Allowed_200.png/revision/latest/scale-to-width-down/1000?cb=20200806153155')
    elif -30 > score >= -35: return show_image('https://external-preview.redd.it/OZGPYpQASrrhEJVKGMHbtKYsL5lS6Vpn1WG2gD_1UFc.jpg?auto=webp&v=enabled&s=8a6c28faa60b9fd35c4fec1bf5fa0a34a70a35b4')
    elif score < -35: return show_image('https://i.redd.it/xf5mv2emtyb71.png')

def show_image(url):
    with urlopen(url) as response:
        image_data = response.read()
    image = Image.open(BytesIO(image_data))
    root = tk.Tk()
    root.title('Image')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()
    root.mainloop()

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
def prPink(skk): return print("\033[95m{}\033[00m".format(skk))
def prPinkNone(skk): return "\033[95m{}\033[00m".format(skk)
def prLCyan(skk): return print("\033[96m{}\033[00m".format(skk))
def prRedBg(skk): return print("\033[41m{}\033[00m".format(skk))
def prGreenBg(skk): return print("\033[42m{}\033[00m".format(skk))

playGame()