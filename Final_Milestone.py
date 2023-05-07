global acceptable_range
acceptable_range=['1','2','3','4','5','6','7','8','9','!']

global used_num
used_num=[]

global gb1
global gb2
global gb3
gb1=['','','']
gb2=['','','']
gb3=['','','']

global gb
gb=['','','','','','','','','']

global count
count=0


#**************************************************************************
while count < 5:
    
    def position_choicep1(): 
            global p1int_choice     
            p1choice=''
        
            
            while p1choice not in acceptable_range:
                p1choice = input('Pick a number player1: ')
          
                if p1choice not in acceptable_range:
                    print('Invalid Choice')
                    
            print(used_num)
            
            used_num.append(int(p1choice))        
            p1int_choice = int(p1choice)       
         
            return p1int_choice
    
    position_choicep1()

    
#*******************************************************************
    def movepiece1(p1int):#Function to move the piece player1 
            gb[p1int-1]='X'
            
            
            if p1int in range(1,4):
                gb1[p1int-1]='X'
                
            elif p1int in range(4,7):
                gb2[p1int-4]='X'
                
            elif p1int in range(7,10):
                gb3[p1int-7]='X'
                
            else:
                pass
           
            print(gb1,'\n',gb2,'\n',gb3)
            #print(gb)  
    movepiece1(p1int_choice)
#********************************************************************

    def position_choicep2(): 
            global p2int_choice     
            p2choice=''
        
            
            while p2choice not in acceptable_range:
                p2choice = input('Pick a number player2: ')
                #print(type(p2))
          
                if p2choice not in acceptable_range:
                    print('Invalid Choice')
                
            used_num.append(int(p2choice))    
            p2int_choice = int(p2choice)
         
            return p2int_choice
    
    position_choicep2()
    
#**************************************************************************

    def movepiece2(p2int):
            
            gb[p2int-1]='O'
            
            if p2int in range(1,4):
                gb1[p2int-1]='O'
                
            elif p2int in range(4,7):
                gb2[p2int-4]='O'
                
            elif p2int in range(7,10):
                gb3[p2int-7]='O'
                
            else:
                pass

            print(gb1,'\n',gb2,'\n',gb3)
              
    movepiece2(p2int_choice)
    

#*********************************************************************************

    def iswinner(gameboard):#Determines who is winner by using GB to find pattern of XXX and OOO
        if gameboard[0]=='X' and gameboard[1]=='X' and gameboard[2]=='X' or gameboard[3]=='X' and gameboard[4]=='X' and gameboard[5]=='X':
            print('WINNER X')
        else:
            print('No Winners')
        #print(gb)
        
        
        
        
    iswinner(gb)













    count+=1