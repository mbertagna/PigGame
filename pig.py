#Michael Bertagna
#2353491
#bertagna@chapman.edu
#CPSC 230: 9:00 AM MWF
#Assignment 4

# 1 start game (while loop containing player and computer turn loops)
# 2 player turn (while loop)
#   2a roll 1-6 and print roll to user
#   2b if roll=1 end turn and give player no additional points
#   2c if roll!=1 add roll to player total score and allow user to hold or roll again
#   2d if player holds end turn and solidify total points
#      if player rolls run the player turn loop again
# 3 computer turn (while loop)
#   3a roll 1-6 and print roll to user
#   3b if roll=1 end turn and give computer no additional points
#   3c if roll!=1 add roll to computer total score and roll again
#   3d if turn total gets to 20 then end turn and print computer hold to user
# 4 if the player total score or computer total score ever 100+ end game and print who won to user



# import modules to be used
import random
import time

# declare variables, so that do not get error when they are used but not declared
# Tot means total solidified score
playerTot=0
aiTot=0
# choice used for player input
choice=0
# roll = random number on dice: 1-6
roll=0
aiTurnTotal=0
playerTurnTotal=0

# while loop will repeat until player or ai get 100 points and win
#else will then run and let player know who has won
while playerTot < 100 and aiTot < 100:

    # stop used to stop player turn if they hold must be reset to 0 before every turn
    stop = 0
    # prompt player to let them know it's their turn
    print('PLAYER TURN')
    # time sleep gives a player a chance to read info before printing anymore
    time.sleep(1)
    # print players total score
    print('PLAYER TOTAL SCORE:', playerTot)
    time.sleep(1)
    #while loop for player's turn: stops is they win (get 100+ pts) or if roll=1 or if they hold(stop=0)
    while playerTot <100 and stop == 0 and roll != 1:
        # roll = random number 1-6
        roll = random.randint(1,6)
        # print player's rollback to them
        print('Player rolled a',roll)
        if roll==1:
            # if roll=1 this will run and player turn score taken away from total score
            playerTot=playerTot-playerTurnTotal
        # if player does not roll one or choose to hold this loop will run
        while roll != 1 and choice != 'h':
            # calculate proposed player total by adding lastest roll
            playerTot = playerTot + roll
            # if player's total score >= 100 the loop will break and then the player turn loop
            # will check its conditions and stop looping as well
            if playerTot >= 100:
                break
            # calculate player turn total for use if player rolls a 1 and turn points must be deducted from total score
            playerTurnTotal = playerTurnTotal + roll
            # prompt player to roll again or hold
            print("Press [r] to roll again, or [h] to hold your current score.")
            choice = input("What would you like to do? ")
            # if choice = r then break out of current loop so main player loop runs again
            if choice == 'r':
                break
            # if choice = h then set stop = 0 which will end player turn bc of player loop conditions
            elif choice == 'h':
                stop = 1
            # if player inputs characters other than r and h tell them to try again and continue current loop
            else:
                print('Invalid Response: Please input [r] or [h].')
    # when the player turn is over let them know and provide them with their total score
    else:
        if playerTot < 100:
            print('PLAYER TURN OVER')
            time.sleep(1)
            print('PLAYER TOTAL SCORE:', playerTot)
            time.sleep(2)

    # set player turn total back to zero
    playerTurnTotal=0
    # set stop to 0 bc served purpose and player turn over
    stop = 0
    # set choice = 0 so that player can choose r or h on next turn
    choice=0
    # set roll = 0 so that computer's turn loop conditions are not immediately ended
    roll = 0

    # if the player has not won, the player will be notified that it is the computer's turn
    # and of the computer's score
    if playerTot < 100:
        print('COMPUTER TURN')
        time.sleep(1)
        print('COMPUTER TOTAL SCORE:', aiTot)

    # computer turn loop: if player or computer has not won and the ai hasn't rolled a won or reached
    # 20 points in a turn the loop will continue
    while aiTot < 100 and playerTot < 100 and roll != 1 and aiTurnTotal < 20:
        # roll = random number 1-6
        roll = random.randint(1,6)
        time.sleep(1)
        # print computer's roll to user
        print('Computer rolled a', roll)
        # if computer rolls 1 subract its turn score
        if roll==1:
            aiTot=aiTot-aiTurnTotal
        # if roll != 1 then all roll to total score and turn total
        if roll != 1:
            aiTot = aiTot + roll
            aiTurnTotal = aiTurnTotal + roll
        # if computer wins break loop/turn
        if aiTot >= 100:
            break
        # if computer gets 20+ points end turn and prompt user that the computer held
        if aiTurnTotal >= 20:
            print('Computer chose to hold.')
    # when computer turn over, if the player or computer has not won yet, print computer turn over to user
    # and computer total score
    else:
        if playerTot < 100:
            print('COMPUTER TURN OVER')
            time.sleep(1)
            print('COMPUTER TOTAL SCORE:', aiTot)
            time.sleep(2)
    # set computer turn total to 0
    aiTurnTotal=0
    # set roll=0 so player loop can run
    roll=0
# else will run when player or computer has won
else:
    # if player won print to player and tell player their total score
    if playerTot >= 100:
        print('PLAYER TOTAL SCORE:', playerTot)
        print('Player Wins!')
    # if computer won tell player the computer won and its score
    elif aiTot >= 100:
        print('COMPUTER TOTAL SCORE:', aiTot)
        print('Computer Wins!')
