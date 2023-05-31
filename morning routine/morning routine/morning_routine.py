print ("alarm")
snooze = input ("sleep longer? yes/no?")
if (snooze == "yes"):
    print ("ask again 10 mins")
    snooze = input ("sleep longer? yes/no?")
    if (snooze == "yes"):
        print ("ask again 10 mins")
        snooze = input ("sleep longer? yes/no?")
        if (snooze == "yes"):
            print ("ask again 10 mins")
if (snooze == "no"):
    print ("go to shower")
shower = input ("shower? yes/no?")
if (shower == "yes"):
    print ("get dressed")
if (shower == "no"):
    print ("get dressed")
sweater = input ("sweater? yes/no")
if (sweater == "yes"):
    print ("downstairs")
if (sweater == "no"):
    print ("downstairs")
