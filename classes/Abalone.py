#include<bits/stdc++.h>
#define int long long
#define ios ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);

import math, copy, discord

class response:
    send_msg=""
    reply_msg=""
    special=0 #0沒事 1刪除遊戲
    def __init__(self,send_msg:str,reply_msg:str,message:discord.message)->None:
        self.send_msg=send_msg
        self.reply_msg=reply_msg
        return
    def add_send(self,add_msg:str)->None:
        self.send_msg+=add_msg
        return
    def add_reply(self,add_msg:str)->None:
        self.reply_msg+=add_msg
        return
    def change(self,send_msg:str,reply_msg:str,s:int)->None:
        self.send_msg=send_msg
        self.reply_msg=reply_msg
        self.special=s
        return

#graph=('💿🈳⭕ ','⚪ ','⚫ ')
graph=('⭕  ','⚽  ','🥎  ','  ')
Situation=("未開始","輪到玩家1","輪到玩家2","等待玩家2加入")
abalone_rules="""
**角力棋規則說明:**
**角力棋**棋與棋盤:
1. 棋: 有黑白兩種顏色各14個
2. 棋盤: 為一個編長5格的正六邊形，如下
```
    . . . . .     
   . . . . . .    
  . . . . . . .   
 . . . . . . . .  
. . . . . . . . . 
 . . . . . . . . 
  . . . . . . . 
   . . . . . . 
    . . . . . 
```
**角力棋**有2種移動方式:
    1. **側移**: 選定相鄰且呈一直線的 1~3 顆棋向任意無棋方向移動一格
    2. **推移**: 選定相鄰且呈一直線的 2~3 顆棋向直線方向推動，自己推動的棋數需多餘敵人阻擋的棋數，且不可遭己方棋阻擋
**角力棋**結束方式:
    敵人遭推出5個棋時獲勝
**輸入** ```//abalone cmd``` 以查看指令方式
"""

abalone_cmd="""
**角力棋**輸入方式:
一律以```//abalone``` 或 ```//角力棋``` 作為相關指令開頭
1. 開始:
    輸入 ```開始``` 或 ```start```
2. 加入:
    輸入 ```加入``` 或 ```join```
3. 求助:
    輸入 ```help```
4. 移動:
```移動 {x1} {y1} {x2} {y2} {移動方向}```
座標如下
```
  0 1 2 3 4 5 6 7 8
0 . . . . .
1 . . . . . .
2 . . . . . . .
3 . . . . . . . .
4 . . . . . . . . .
5   . . . . . . . .
6     . . . . . . .
7       . . . . . .
8         . . . . .
```
方向如下
```
    4   5
   3  .  0
    2   1
```
5. 退出:
    輸入 ```退出``` 或 ```quit```
6. 查看指令
    輸入 ```指令``` 或 ```cmd```
"""

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
    if(player==-1):
        return ' '
    else:
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
    situation=0
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
        if(self.block[p.x][p.y]==-1):
            return ' '
        else:
            return graph[self.block[p.x][p.y]]

    def output(self)->str:
        outputstring=" A B C  D E F G H  I  J K L M N  O P Q\n"
        p=pos(0,0)
        while(p.y<4):
            p.x=0
            outputstring+=str(p.y)
            outputstring+=graph[3]*(4-p.y)
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
        outputstring="```\n"+outputstring+"```\n"
        if self.score[1]==self.score[0]:
            outputstring+=f" <@{self.player1}> 獲勝\n遊戲結束"
            return outputstring
        elif self.score[2]==self.score[0]:
            outputstring+=f" <@{self.player2}> 獲勝\n遊戲結束"
            return outputstring
        #outputstring=f"<@{self.player1}> 目前{self.score[1]}分\n<@{self.player2}> 目前{self.score[2]}分\n"
        elif self.score[1]==self.score[2]:
            outputstring+=f"<@{self.player1}> & <@{self.player2}> 皆得{self.score[1]}分\n"
        elif self.score[1]>self.score[2]:
            outputstring+=f"<@{self.player1}> 目前{self.score[1]}分\n領先 <@{self.player2}> {self.score[1]-self.score[2]}分\n"
        elif self.score[1]<self.score[2]:
            outputstring+=f"<@{self.player2}> 目前{self.score[2]}分\n領先 <@{self.player1}> {self.score[2]-self.score[1]}分\n"
        if self.situation==1:
            outputstring+=f"輪到玩家1 <@{self.player1}>"
        elif self.situation==2:
            outputstring+=f"輪到玩家2 <@{self.player2}>"
        elif self.situation==0:
            outputstring+="結束"
        elif self.situation==3:
            outputstring+=f"等待玩家二加入"
        return outputstring

    def move1(self,player:int,p:pos,direction:int):
        next_pos=copy.deepcopy(p)
        if(next_pos.next(direction)=="Invalid direction"):
            print("Move Failed->Invalid direction")
            return "Move Failed->Invalid direction"
        elif (player!=self.block[p.x][p.y]):
            return "Move Failed->Not Your Chess"
        elif(next_pos.check()==False):
            print("Move Failed->Invalid next position")
            return "Move Failed->Invalid next position"
        elif(p.check()==False):
            print("Move Failed->Invalid position")
            return "Move Failed->Invalid position"
        elif(self.block[p.x][p.y]!=1 and self.block[p.x][p.y]!=2):
            print("Move Failed->Block Empty")
            return "Move Failed->Block Empty"
        elif(self.block[next_pos.x][next_pos.y]!=0):
            print("Move Failed->Invalid Next Block Filled")
            return "Move Failed->Invalid Next Block Filled"
        else:
            self.block[next_pos.x][next_pos.y]=self.block[p.x][p.y]
            self.block[p.x][p.y]=0
        return "移動成功"

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
                return "移動成功"
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
                return "移動成功"#
        else:
            next_pos1=copy.deepcopy(p1)
            next_pos2=copy.deepcopy(p2)
            next_pos1.next(direction)
            next_pos2.next(direction)
            if(self.block[next_pos1.x][next_pos1.y]!=0 or self.block[next_pos2.x][next_pos2.y]!=0):
                print("Move Failed->Not Empty Block")
                return "Move Failed->Not Empty Block"
            if(len==3):
                next_pos_middle=copy.deepcopy(p_middle)
                next_pos_middle.next(direction)
                if(self.block[next_pos_middle.x][next_pos_middle.y]!=0):
                    print("Move Failed->Not Empty Block")
                    return "Move Failed->Not Empty Block"
                temp=self.move1(player,p_middle,direction)
            self.move1(player,p1,direction)
            self.move1(player,p2,direction)
            return "移動成功"

    def play(self,message:discord.message, w:str)->response:
        R=response("","",message)
        if w=="開始" or w=="start":
            if self.situation==0:
                self.player1=message.author.id
                self.situation=3
                R.reply_msg=f"玩家一 <@{self.player1}> 已加入\n"
            else:
                R.reply_msg="遊戲已經開始\n"
                return R
        elif w[0:4:1]=="join" or w[0:2:1]=="加入":
            if self.situation==0 or self.situation==3:
                new_join=0
                if w[0:4:1]=="join":
                    w=w[4:len(w):1]
                else:
                    w=w[2:len(w):1]
                w=w.strip()
                if w=="":
                    if self.situation==0:
                        self.player1=message.author.id
                        self.situation=3
                        R.reply_msg+=f"玩家一 <@{self.player1}> 已加入\n"
                    elif self.situation==3:
                        if self.player1==message.author.id:
                            R.reply_msg+=f"<@{self.player1} 你不能和自己玩"
                        self.player2=message.author.id
                        self.situation=1
                        R.reply_msg+=f"玩家二 <@{self.player2}> 已加入\n"
                        self.new_game(1)
                        R.send_msg+=self.output()+"\n遊戲開始"
                elif w[0:2:1]=="<@":
                    L=len(w)
                    i=2
                    while i<L:
                        if w[i]=='>':
                            if w[2:i+1:1].isdigit()==False:
                                R.change("","ERROR",1)
                                return R
                            elif self.situation==0:
                                self.player1=int(w[2:i+1:1])
                                self.situation==3
                                new_join+=1
                                R.reply_msg+=f"玩家一 <@{self.player1}> 已加入\n"
                                if i==L:
                                    break
                                w=w[i+1:len(w):1]
                                w=w.strip()
                                L=len(w)
                                i=2
                                if L<2:
                                    break
                                if w[0:2:1]!="<@":
                                    break
                            elif self.situation==3:
                                self.player2==int(w[2:i+1:1])
                                self.situation==1
                                new_join+=2
                                self.new_game(1)
                                R.send_msg+=self.output()
                                R.reply_msg+=f"玩家2 <@{self.player2}> 加入遊戲\n遊戲開始"
                                if i==L:
                                    break
                                w=w[i+1:len(w):1]
                                w=w.strip()
                                L=len(w)
                                i=2
                                if L<2:
                                    break
                                if w[0:2:1]=="<@":
                                    R.change("","一場比賽只能有兩名成員參加\n請重新加入遊戲",1)
                                    return R
                        i+=1
        elif w=="help":
            R.send_msg="輸入 ```//abalone rule``` 查看遊戲規則\輸入 ```//abalone cmd``` 查看指定運作方式"
        elif w[0:4:1]=="move" or w[0:2:1]=="移動":
            if w[0:2:1]=="移動":
                w=w[2:len(w):1]
            else:
                w=w[4:len(w):1]
            w=w.strip()
            d=w.split()
            print(d)
            if (self.situation==1 and self.player1!=message.author.id) or (self.situation==2 and self.player2!=message.author.id) or (self.situation!=1 and self.situation!=2):
                R.change(f"{self.player1} {self.player2} {message.author.id} {self.situation}","只能移動自己的棋",0)
                return R
            for i in d:
                if i.isdigit()==False:
                    R.change("","輸入錯誤，請重新輸入\n請輸入5個數字 兩端xy座標 與移動方向",0)
                    return R 
            if len(d)==3:
                p1=pos(int(d[0]),int(d[1]))
                now=self.move1(self.situation,p1,int(d[2]))
                R.reply_msg+=now
                if now=="移動成功":
                    self.situation=2-(self.situation+1)%2
            elif len(d)==5:
                p1=pos(int(d[0]),int(d[1]))
                p2=pos(int(d[2]),int(d[3]))
                now=self.move(self.situation,p1,p2,int(d[4]))
                R.reply_msg+=now
                if now=="移動成功":
                    self.situation=2-(self.situation+1)%2
            else:
                R.reply_msg+="輸入錯誤，請重新輸入\n請輸入5個數字 兩端xy座標 與移動方向"
            if self.score[1]==self.score[0] or self.score[2]==self.score[0]:
                R.special=1
            R.send_msg+=self.output()
        elif w[0:4:1]=="quit" or w[0:2:1]=="退出":
            if message.author.id!=self.player1 and message.author.id!=self.player2:
                R.reply_msg+=f"<@{message.author.id}> 你沒有加入，無法退出"
                return R
            
            R.special=1
        elif w[0:3:1]=="cmd":
            R.send_msg+=abalone_cmd
        elif w[0:4:1]=="rule":
            R.send_msg+=abalone_rules
        elif w[0:3:1]=="now" or w[0:5:1]=="board":
            R.send_msg+=self.output()
        else:
            R.reply_msg="輸入錯誤，請輸入```//abalone help```得知使用方式"
        #print(R.send_msg,R.reply_msg,R.special)
        return R
        

