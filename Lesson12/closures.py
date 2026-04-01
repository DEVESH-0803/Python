# Closure is a fxn having acces to scope of its parent fxn
#fxn after the parent fxn has returned

def parent_fxn(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1
       
        if coins > 1:
            print(f"{person} has {coins} coins")
        elif coins == 1:
            print(f"{person} has {coins} coin.")
        else:
            print(f"{person} has no coins left.")   

    return play_game

John = parent_fxn("John") # storing play_game() in John
John() # This is : play_game()
John()  
John()  


# Flow of execution:
# parent_fxn("John") -> returns play_game  
# John = play_game  
# John() -> calls play_game

Emily = parent_fxn("Emily")
Emily()