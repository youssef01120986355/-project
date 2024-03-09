print("welcome in Number scrabble")
def sturction_of_game():
 print("Number scrabble is played with the list of numbers between 1 and 9.Each player takesturns picking a number from the list.Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game.However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
sturction_of_game()
begain_game=input("to begain the game,please enter any key")
list_of_numbers=[1,2,3,4,5,6,7,8,9]
player1=0
player2=0
def player1_input():
 global player1
 player1_num=int(input("enter your num,player1"))
 if 1<= player1_num <=9 and player1_num in list_of_numbers:
  list_of_numbers.remove(player1_num)
  player1=player1+player1_num
  return player1
 else:
  print("the number is wrong ,try again ")
  player1_num=int(input(" player1,please enter again number and follow the struction of game"))
  list_of_numbers.remove(player1_num)
def player2_input():
 global player2
 player2_num=int(input("enter your num,player2"))
 if 1<= player2_num <=9 and player2_num in list_of_numbers:
  list_of_numbers.remove(player2_num)
  player2=player2+player2_num
  return player2
 else:
  print("the number is wrong ,try again ")
  player2_num=int(input(" player2,piease inter again number and follow the struction of game"))
  list_of_numbers.remove(player2_num)  
def player1_winner_winner():
 if player1==15:
  print("player1 is the winner")  
def player2_winner_winner():
 if player2==15:
  print("player2 is the winner")  
def the_play() :
 count=0
 for player in range (0,3) :
  print("the list of number :",list_of_numbers)
  player1_input()
  count=count+1
  if player1==15:
   print("player1 is the winner")
   break
  player2_input()
  if player2==15:
   print(" player2 is the winner ")
   break
  if count==3:
   for Q in range (0,1):
    print("the list of numbers",list_of_numbers)
    player1_input()
    if player1==15:
     print("player1 is the winner")
     break
    player2_input()
    player2_winner_winner()
the_play()    
if player1!=15 and player2!=15:
 print("draw") 
while True:
 restart_theplay=input(" if you like to play another game please,press on any key expect no if you are busy write no") 
 if restart_theplay=="no" or restart_theplay=="NO" or restart_theplay=="nO" or restart_theplay=="No":
  print("see you soon , thank you")
  break
 else:
  list_of_numbers=[1,2,3,4,5,6,7,8,9]
  player1=0
  player2=0
  the_play()
 
  

   
  
