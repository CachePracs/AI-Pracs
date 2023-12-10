def moveTower(height,Beg,Des,Aux):
    if(height>=1):
        moveTower(height-1,Beg,Aux,Des)
        print("Moving disk from",Beg,"to",Des)
        moveTower(height-1,Aux,Des,Beg)
moveTower(3,"A","B","C")
