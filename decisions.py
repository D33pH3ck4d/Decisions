import time,math,random
##im sorry.##
start=input('start? y or n : ')
if start=='y':
    print('game, START!')
    grandma='normal'
    debugchange='error'
    debugchange2='error'
    debugdelete='NFA'
    db='off'
    dm='off' 
    snacks=0
    money=20
    health=30
    reputation=100
    print('money:',money)
    print('health:',health)
    time.sleep(0.5)
    debug=input('put in special passcode : ')
    if debug=='turnondebug':
        print('ERROR')
        debugchange='NFA'
    if debug=="121712":
        db='on'
        print('DEBUG ON')
    if debug=="doublemoney":
        dm="on"
    if debug=='passcode':
        print('Stop it. No special cheat codes for you!')
    if debug=='itsmybirthday':
        print('Happy Birthday!')
        reputation+=20
        snacks+=3
    if debug=='no':
        print('yes')
        health-=10
    if debug=='grandma is cool':
        money+=25
        health+=10
        grandma='cool'
    if debug=='secretcheatcodethatiforgotwasinthegamebutproblablygivesyoualotoffreemoneythatyoudidnotearn123':
        print('Ok you looked in the code for that one')
        money+=9999 
    if debug=='eleanor':
        money=0
        health=1
        reputation=0
        print('bruh')
    print('Your friend says to go in a sketchy building. will you?')
    buildyn=input('y or n : ')
    if buildyn=='y':
        reputation-=5
        print('its a illegal casino.')
        time.sleep(0.2)
        gamble=input('gamble? Dont do it its broken. y or n : ')
        if gamble=='y':
            if db=='on':
                randnum=int(random.random())+1
                randnumf=round(round(round(round(randnum))))
                print(randnumf)
                randnumyn=input('type a number, 0 or 1. : ')
                if randnumyn==randnumf:
                    print('you won!')
                    money+=10
                    if dm=='on':
                        money+=10
                    print('money:',money)
                else:
                    print('you lost!')
                    money-=10
                    #debug mode feature  \/  \/  \/
                    money+=20
                    print('money:',money)
        else:
            if gamble=='gamblenow':
                print('ERROR')
                debugchange2='NFA'
            #print('you couldve won money...')
            print('Welp ok.')
    else:
        print('you steer clear of the building.')
    print('you go to the store, buy snacks? 15 dollars each.')
    snack=input('y or n : ')
    if snack=='y':
        if money>=15:
            snacks+=1
            money-=15
            reputation+=5
            print('you bought 1 snack.')
            print('money:',money)
        else:
            print('not enough money!')
            print('money:',money)
            reputation-=10
    else:
        print('you did not buy snacks.')
    print('you pick up a fortune cookie from the sidewalk. read it?')
    readcooke=input('y or n : ')
    if readcooke=='y':
        a=random.sample(range(1,99),6)
        print('your lucky numbers are :',a)
    else:
        print('you did not read the cookie.')
    print('you found a phone. use it?')  
    usephone=input('y or n : ')
    if usephone=='y':
        password=23
        passatt=input('what is 8x2-9+16 from left to right? : ')
        if passatt==password:
            print('there is money on the phone. transfer it?')
            tphone=input('y or n : ')
            if tphone=='y':
                money+=10
                if dm=='on':
                    money+=10
                reputation-=15
                print('you transferred the money.')
                print('money:',money)
            else:
                print('you did not transfer the money.')
        else:
            if db=='on':
                print('there is money on the phone. transfer it?')
                tphone=input('y or n : ')
                if tphone=='y':
                    money+=10
                    reputation-=15
                    print('you transferred the money.')
                    print(money)
                else:
                    print('you did not transfer the money.')
            else:
                if grandma=='cool':
                    print('there is money on the phone. transfer it?')
                    tphone=input('y or n : ')
                    if tphone=='y':
                        money+=10
                        reputation-=10
                        print('you transferred the money.')
                        print('money:',money)
                    else:
                        print('you did not transfer the money.')
                else:
                    if passatt=='DELETEALTF4':
                        print('WHYSTOPNOW')
                print('WRONG PASSWORD')
    else:
        print('you did not use the phone.')
    print('you see an ice cream truck. go to it?')
    icec=input('y or n : ')
    if icec=='y':
        print('You see a kid without enough money. Help the kid? 5 dollars.')
        helpkid=input('y or n : ')
        if helpkid=='y':
            if money >= 5:
                reputation=+10
                print('you bought the kid ice cream.')
            else:
                reputation=-20
                print('you dont have enough money.')
                #-10 min rep here
        else:
            if helpkid =='HELPME':
                print('WHY WOULD YOU DO THIS')
                debugdelete='NFA'
            print('you did not help the kid.')
    