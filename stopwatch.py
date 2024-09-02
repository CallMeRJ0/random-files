import time

timer_legnth=str(input("How long would you like your timer to be?\nType it as (Amount of seconds, minutes or hours) (s / m / h)\n"))
if "s" in timer_legnth:
    timer_list=timer_legnth.split()
    timer_legnth=timer_list[0]
    timer_legnth=float(timer_legnth)*1
    timer_list.pop()
    while int(timer_legnth)>-1:
        print("You have "+str(timer_legnth)+" seconds left.")
        timer_legnth=int(timer_legnth)-1
        time.sleep(1)
        if timer_legnth==0 or timer_legnth < 0:
            print("Your countdown has ended!")
            break
elif "m" in timer_legnth:
    timer_list=timer_legnth.split()
    timer_legnth=timer_list[0]
    timer_legnth=float(timer_legnth)*60
    timer_list.pop()
    while int(timer_legnth)>-1:
        print("You have "+str(timer_legnth)+" seconds left.")
        timer_legnth=int(timer_legnth)-1
        time.sleep(1)
        if timer_legnth==0 or timer_legnth < 0:
            print("Your countdown has ended!")
            break
elif "h" in timer_legnth:
    timer_list=timer_legnth.split()
    timer_legnth=timer_list[0]
    timer_legnth=float(timer_legnth)*3600
    timer_list.pop()
    while int(timer_legnth)>-1:
        print("You have "+str(timer_legnth)+" seconds left.")
        timer_legnth=int(timer_legnth)-1
        time.sleep(1)
        if timer_legnth==0 or timer_legnth < 0:
            print("Your countdown has ended!")
            break
