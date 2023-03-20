#include<bits/stdc++.h>
#define int long long
#define ios ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
#define ull unsigned long long
import math, copy
graph=('⭕  ','⚽  ','🥎  ','  ')

class pos:
    x=-1
    y=-1
    def __init__(self,X:int,Y:int):
        self.x=X
        self.y=Y
        return
    def next(self,direction:int):
        if(direction==5):
            self.y-=1
        elif(direction==0):
            self.x+=1
        elif(direction==1):
            self.x+=1
            self.y+=1
        elif(direction==2):
            self.y+=1
        elif(direction==3):
            self.x-=1
        elif(direction==4):
            self.x-=1
            self.y-=1
        else:
            print("Invalid direction")
            return "Invalid direction"
        if(self.x>=0 and self.x<9 and self.y>=0 and self.y<9):
            return self
        else:
            return ("No This Block")
    def check(self)->bool:
        if self.x<0 or self.y<0 or self.x>=9 or self.y>=9 or abs(self.x-self.y)>4:
            return False
        else:
            return True

    def check(self)->bool:
        if(self.x>=0 and self.y>=0 and self.x<9 and self.y<9):
            return True
        else:
            return False

def pos_distance(p1:pos,p2:pos):
    if(p1.x!=p2.x and p1.y!=p2.y and p1.x-p1.y!=p2.x-p2.y):
        print("Failed->Two Positions not at the same line")
        return "Failed->Two Positions not at the same line"
    elif(p1.check() and p2.check()):
        return max(abs(p1.x-p2.x),abs(p1.y-p2.y))+1
    else:
        print("Failed->Position ERROR")
        return "Failed->Position ERROR"

def pos_direction(p1:pos,p2:pos):
    c=pos_distance(p1,p2)
    if(type(c)!=int):
        return c
    elif(c==1):
        print("Invalid Direction->Same Position")
        return "Invalid Direction->Same Position"
    elif(p1.x==p2.x):
        return 2
    elif(p1.y==p2.y):
        return 0
    elif(p1.x-p1.y==p2.x-p2.y):
        return 1
    else:
        print("Never Happen")
        return "Never Happen"

def player_print(player:int)->str:
    return graph[player]


class Abalone:
    block=[[0]*9 for i in range(9)]
    for i in range(0,4):
        for j in range(5+i,9):
            block[j][i]=-1
    for i in range(1,5):
        for j in range(0,i):
            block[j][i+4]=-1
    score=[5,0,0]

    def new_game(self,x):
        score=[5,0,0]
        for i in range(0,9):
            for j in range(0,9):
                if(self.block[i][j]!=-1):
                    self.block[i][j]=0
        if(x==1):
            for i in range(0,4):
                for j in range(i,5):
                    self.block[j][i]=1
                    self.block[8-j][8-i]=2

    def print1(self,p:pos)->str:
        if(type(p)!=pos):
            print("Invalid position")
            return
        return graph[self.block[p.x][p.y]]

    def output(self)->str:
        outputstring=" A B C  D E F G H  I  J K L M N  O P Q\n"
        p=pos(0,0)
        while(p.y<4):
            p.x=0
            outputstring+=str(p.y)
            outputstring+=graph[-1]*(4-p.y)
            while(p.x<9):
                outputstring+=self.print1(p)
                p.x+=1
            outputstring+='\n'
            p.y+=1
        while(p.y<9):
            p.x=0
            outputstring+=str(p.y)
            while(p.x<9):
                outputstring+=self.print1(p)
                p.x+=1
            outputstring+='\n'
            p.y+=1
        outputstring+="player white score=="+str(self.score[1])+"\tplayer black score=="+str(self.score[2])
        if(self.score[1]==self.score[0]):
            outputstring+="White Win\n"
        elif(self.score[2]==self.score[0]):
            outputstring+="Black Win\n"
        return outputstring

    def move1(self,player:int,p:pos,direction:int):
        next_pos=copy.deepcopy(p)
        if(next_pos.next(direction)=="Invalid direction"):
            print("Move Failed->Invalid direction")
            return "Move Failed->Invalid direction"
        elif(next_pos.check()==False or p.check()==False):
            print("Move Failed->Invalid next position")
            return "Move Failed->Invalid next position"
        elif(self.block[p.x][p.y]!=player):
            print("Move Failed->Not Your Block")
            return "Move Failed->Not Your Block"
        elif(self.block[next_pos.x][next_pos.y]!=0):
            print("Move Failed->Invalid Next Block Filled")
            return "Move Failed->Invalid Next Block Filled"
        else:
            self.block[next_pos.x][next_pos.y]=self.block[p.x][p.y]
            self.block[p.x][p.y]=0
        return True

    def move(self,player:int,p1:pos,p2:pos,direction:int):
        if(player==1):
            enemy=2
        elif(player==2):
            enemy=1
        else:
            print("Move Failed->ERROR Player")
            return "Move Failed->ERROR Player"
        if(direction<0 or direction>=6):
            print("Direction Failed")
            return "Direction Failed"
        len=pos_distance(p1,p2)
        if(type(len)!=int):
            return len
        if(len==1):
            return self.move1(player,p1,direction)
        elif(len==3):
            p_middle=pos((p1.x+p2.x)//2,(p1.y+p2.y)//2)
            if(self.block[p_middle.x][p_middle.y]!=player or self.block[p1.x][p1.y]!=player or self.block[p2.x][p2.y]!=player):
                print("Move Failed->Not Your Chess")
                return "Move Failed->Not Your Chess"
        elif(len==2):
            if(self.block[p1.x][p1.y]!=player or self.block[p2.x][p2.y]!=player):
                print("Move Failed->Not Your Chess")
                return "Move Failed->Not Your Chess"
        else:
            print("Move Failed->Too Long")
            return "Move Failed->Too Long"
        if(pos_direction(p1,p2)==direction%3):
            if((direction<3 and (p1.x<p2.x or (p1.x==p2.x and p1.y<p2.y))) or (direction>=3 and (p1.x>p2.x or (p1.x==p2.x and p1.y>p2.y)))):
                temp=p1
                p1=p2
                p2=temp
            next_pos=copy.deepcopy(p1)
            next_pos.next(direction)
            if (next_pos.check()==False):
                return "Move Failed->Not Empty Block"
            elif(self.block[next_pos.x][next_pos.y]==0):
                self.block[next_pos.x][next_pos.y]=player
                self.block[p2.x][p2.y]=0
                return True
            else:
                enemy_next_p=copy.deepcopy(next_pos)
                enemy_len=0
                while(self.block[enemy_next_p.x][enemy_next_p.y]==enemy):
                    enemy_len+=1
                    if(enemy_next_p.next(direction)=="No This Block"):
                        break
                if(pos_distance(enemy_next_p,next_pos)):
                    print("Not Long Enough")
                    return "Not Long Enough"
                elif(enemy_next_p.check()==False):
                    enemy_next_p.next((direction+3)%6)
                    self.score[player]+=1
                elif(self.block[enemy_next_p.x][enemy_next_p.y]==player):
                    print("Move Failed->Your Own Chess")
                    return "Move Failed->Your Own Chess"
                elif(enemy_len>=len):
                    print("Move Failed->Too Short")
                    return "Move Failed->Too Short"
                else:
                    self.block[enemy_next_p.x][enemy_next_p.y]=enemy
                self.block[next_pos.x][next_pos.y]=player
                self.block[p2.x][p2.y]=0
                return True#
        else:
            next_pos1=copy.deepcopy(p1)
            next_pos2=copy.deepcopy(p2)
            next_pos1.next(direction)
            next_pos2.next(direction)
            if(self.block[next_pos1.x][next_pos1.y]!=0 or self.block[next_pos2.x][next_pos2.y]!=0 or next_pos1.check()==False or next_pos2.check()==False):
                print("Move Failed->Not Empty Block")
                return "Move Failed->Not Empty Block"
            if(len==3):
                next_pos_middle=copy.deepcopy(p_middle)
                next_pos_middle.next(direction)
                if(self.block[next_pos_middle.x][next_pos_middle.y]!=0 or next_pos_middle.check):
                    print("Move Failed->Not Empty Block")
                    return "Move Failed->Not Empty Block"
                temp=self.move1(player,p_middle,direction)
            self.move1(player,p1,direction)
            self.move1(player,p2,direction)
            return True

    def play1(self,player:int)->None:
        if(player!=1 and player!=2):
            return "Play Failed->Invalid Player"
        while(True):
            w=input(f"Player {player_print(player)}Start Play\n")
            data=w.split(' ')
            if(len(data)==5):
                p1=pos(int(data[0]),int(data[1]))
                p2=pos(int(data[2]),int(data[3]))
                if(self.move(player,p1,p2,int(data[4]))==True):
                    return True
            print(self.output())
            print("ERROR Please Input Again\n")
        return False

    def play(self,type=1)->None:
        self.new_game(type)
        while(self.score[1]!=self.score[0] or self.score[2]!=self.score):
            print(self.output())
            self.play1(1)
            print(self.output())
            self.play1(2)
        if(self.score[1]==self.score[0]):
            print("Player 1 Win")
        else:
            print("Player 2 Win")
        return 
