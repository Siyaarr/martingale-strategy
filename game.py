import hashlib
#import multithreading


server_seed = "49dd413ab6beba5dc9d92bfc64fba04981336fc252c9737c17916d4ebde35125"
public_seed = "3420053526"
startRound = 6302656

############ 1 000 000 000
roundRange = 100000000

Step = 1

##########


bonusCount = 0
orangeCount = 0
blackCount = 0

rollList1 = []
rollList2 = []

#function where bonus is as orange

def checkColor1(roll):

    if (roll == 0):

        global bonusCount
        bonusCount += 1
        rollList1.append("o")

        return

    elif (roll >= 1 and roll <= 7):

        global orangeCount
        orangeCount += 1
        rollList1.append("o")
        return

    elif (roll >= 8 and roll <= 14):

        global blackCount
        blackCount += 1
        rollList1.append("b")

        return

#function where bonus is as black

def checkColor2(roll):

    if (roll == 0):

        rollList2.append("b")
        return

    elif (roll >= 1 and roll <= 7):

        rollList2.append("o")
        return

    elif (roll >= 8 and roll <= 14):

        rollList2.append("b")
        return





for i in range(roundRange):
    newRound = startRound + Step

    strNewRound = str(newRound)

    line = "-"

    combinedString = server_seed + line + public_seed + line + strNewRound

    shaVersion = hashlib.sha256(combinedString.encode()).hexdigest()

    roll = int(shaVersion[0:8], 16) % 15

    #print(roll)

    checkColor1(roll)
    checkColor2(roll)

    Step += 1


print(f"Bonus: {bonusCount}")
print(f"Orange: {orangeCount}")
print(f"Black: {blackCount}")

rollListString1 = ''.join([str(elem) for elem in rollList1])
rollListString2 = ''.join([str(elem) for elem in rollList2])

#print(rollListString)

def findLongestNextToEachOther(string):
  
    ans, temp = 1, 1
  
    for i in range(1, len(string)):
          
        if (string[i] == string[i - 1]):
            temp += 1

        else:
            ans = max(ans, temp)
            temp = 1
  
    ans = max(ans, temp)
  
    return ans
  
print(f"Longest in row with bonuses being orange: {findLongestNextToEachOther(rollListString1)}")
print(f"Longest in row with bonuses being black: {findLongestNextToEachOther(rollListString2)}")
  