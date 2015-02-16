from random import randint


ivpts = 1001
mapts = 1001

while True:

    ivscore = 0
    icounter = 1

    while icounter<= 5:
        ivdice = randint(1,6)
        ivscore = ivscore + ivdice
        icounter+=1


    if ivpts>0:
        ivpts = ivpts - ivscore
    else:
        ivpts = ivpts + ivscore

    print("Ivan's dice sum is: "+str(ivscore) + "and his points are: "+str(ivpts))
    if ivpts == 0:
        break

    mascore = 0
    mcounter = 1

    while mcounter <=5:
        madice = randint(1,6)
        mascore = mascore + madice
        mcounter+=1

    if mapts>0:
        mapts = mapts - mascore
    else:
        mapts = mapts + mascore

    print("Maria's dice sum is: "+str(mascore) + "and her points are: "+str(mapts))
    if mapts == 0:
        break


if ivpts == 0:
    print("The winner is Ivan")
else:
    print("The winner is Maria")
