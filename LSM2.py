def last_Man_Standing(balls_given, player_first):
    #bool_player = 0 # false --> Lili 
    


    if(player_first == 1):
        if(balls_given % 3 == 0):
            print("Lili")
        else:
            print("lala")
        # bool_player = True
    else:
        if(balls_given % 3 == 0):
            print("Lala")
        else:
            print("Lili")
        # bool_player = False

        '''
        for i in range(1, balls_given):
        bool_player = not bool_player
        

        
        '''
    
    # if(bool_player == True):
    #     return "Lala"
    # else:
    #     return "Lili"



integers = input("Input the balls given and the player who stars first, with the format (N, C): ").strip()
n, c = map(int, integers.split(','))


last_Man_Standing(n, c)