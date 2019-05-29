import Misere_Env as me
grid = me.createGame()
agrid = me.createAvailableSpaces(grid)


while(len(agrid) > 0):
    me.printGridPretty(grid)
    me.printAvailableSpaces(agrid)

    value = int (input("enter an available int: "))

    if( value in agrid):
        grid = ( me.input( grid, value))
        agrid = me.updateAvailableSpaces(grid, agrid)
    else:
        print("youre an idiot")

print("game ended")
