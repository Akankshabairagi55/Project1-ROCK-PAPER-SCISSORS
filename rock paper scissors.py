#Project for Rock,Paper, Scissor Game:-

#importing random library
import random
print("***Welcome to the Game Rock✊  Paper🖐️  Scissor✌️ ***")
print("Lets play the Game!!")

#taking list and dictionary with emojis for input
list=["Rock","Paper","Scissor"]
dic={"Rock":"✊",
    "Paper":"🖐️",
    "Scissor":"✌️"}

#initialize count variables for counting computer score, player score and tie score also take empty string for exit or yes condition.
c=""
c_win=0
u_win=0
tie=0


#taking input for number of times  user  want to play the game.
turn=int(input("Enter number of times you want to play: "))

#loop for whole number of turns and till all conditions becomes true:
while turn:

        while True:
                print("---------------------------------------------------------")

#taking user Input:                
                user_in=input("Enter Rock,Paper or Scissor: ")
                if(user_in=="Rock"or user_in=="Paper"or user_in=="Scissor"):
                        break
                else:
                        print("Enter Valid input🫤")
                      
#applying library and take input from computer                        
        u_in=user_in[:]
        com_in=random.randint(0,2)
        c_in=list[com_in]
        if(user_in=="Rock"):
                user_in=dic["Rock"]
        elif(user_in=="Paper"):
                user_in=dic["Paper"]
        elif(user_in=="Scissor"):
                user_in=dic["Scissor"]
        print("User input: ",user_in)
        if(com_in==0):
                com_in=dic["Rock"]
        elif(com_in==1):
                com_in=dic["Paper"]
        elif(com_in==2):
                com_in=dic["Scissor"]
        print("Computer input: ",com_in)

#checking for all 9 conditions of game and increasing count according to that:
        
        if(c_in=="Rock" and u_in=="Paper"):
                
                u_win+=1
        elif(c_in=="Paper" and u_in=="Rock") :
                
                c_win+=1
        elif(c_in=="Paper" and u_in=="Scissor"):
                
                u_win+=1
        elif(c_in=="Scissor" and u_in=="Paper"):
               
                c_win+=1
        elif(c_in=="Rock" and u_in=="Scissor"):
                
                c_win+=1
        elif(c_in=="Scissor" and u_in=="Rock"):
                
                u_win+=1
        elif(c_in=="Paper" and u_in=="Paper"):
                tie+=1
        elif(c_in=="Scissor" and u_in=="Scissor"):
                tie+=1
        elif(c_in=="Rock" and u_in=="Rock"):
                tie+=1
        turn-=1
        
        if(turn==0):
                print("---------------------------------------------------------")
#asking by if conditions whether the users want to play or exit and then ends the while loop!!               
                
                c=input("Do you want to play again? type Yes to play else type Exit: ")
                if(c=="Yes"):
                        turn=int(input("Enter no of times you want to play: "))
                else:
                        c=="Exit"
                        break
print("Okk Byee!! Come again when You want to play😉 !!")
print("---------------------------------------------------------")

#printing final result with all the counts of tie's ,player score and computer score!!

print("****❤️ Final Result of the Game❤️ ****")
print("---------------------------------------------------------")
print("Computer Score: ",c_win)
print("Your Score: ",u_win)
print("Number of Tie: ",tie)
print("---------------------------------------------------------")

#print who wins in whole game or is it tie!!

if u_win>c_win:
        print("Hurray!!🥳 You Won with ",u_win," point.")
elif u_win<c_win:
        print("Ohh no!!🥹 Computer Won with ",c_win," point.")
else:
        print("Oops😕 It's a Tie!!")





        
        