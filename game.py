import hashlib
#import multithreading


server_seed = "49dd413ab6beba5dc9d92bfc64fba04981336fc252c9737c17916d4ebde35125"
public_seed = "3420053526"
startRound = 6302656

roundRange = 10000

Step = 1

##########


bonusCount = 0
orangeCount = 0
blackCount = 0

rollList = []

def checkColor(roll):

    if (roll == 0):

        global bonusCount
        bonusCount += 1
        rollList.append("x")

        return

    elif (roll >= 1 and roll <= 7):

        global orangeCount
        orangeCount += 1
        rollList.append("o")
        return

    elif (roll >= 8 and roll <= 14):

        global blackCount
        blackCount += 1
        rollList.append("b")

        return



for i in range(roundRange):
    newRound = startRound + Step

    strNewRound = str(newRound)

    line = "-"

    combinedString = server_seed + line + public_seed + line + strNewRound

    shaVersion = hashlib.sha256(combinedString.encode()).hexdigest()

    roll = int(shaVersion[0:8], 16) % 15

    #print(roll)

    checkColor(roll)

    Step += 1


print(f"Bonus: {bonusCount}")
print("Orange:", orangeCount)
print("Black:", blackCount)

rollListString = ''.join([str(elem) for elem in rollList])

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
  
print(findLongestNextToEachOther(rollListString))
  