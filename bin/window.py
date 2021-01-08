# This file shows examples of how to use the sliding window algorithm



# below find the max sum of range of k numbers in array
def slidingWindowHighestWindow(array,k):
    highestSum=0
    head=0

    for i in range(k):
        highestSum+=array[i]

    tempHighest=highestSum

    for j in range(k,len(array)):
        tail = array[j]
        tempHighest+=tail
        tempHighest-=array[head]

        head+=1

        highestSum=max(tempHighest,highestSum)

    print(highestSum)


def slidingWindowLowestWindow(array,k):
    head=0
    lowestWindow=0

    for i in range(k):
        lowestWindow+=array[i]
    tempLowest=lowestWindow

    for j in range(k,len(array)):
        tail = array[j]
        tempLowest+=tail
        tempLowest-=array[head]
        head+=1

        lowestWindow=min(tempLowest,lowestWindow)

    print(lowestWindow)

def howManyWindowsWithTotalGreaterThanVal(array,k,val):
    head=0
    temp=0
    ans=0

    for i in range(k):
        temp+=array[i]

    if(temp>val):
        ans+=1

    for j in range(k,len(array)):
        tail=array[j]
        temp+=tail
        temp-=array[head]
        head+=1

        if(temp>val):
            ans+=1

    print(ans)

def printAllSubArrays(array,k):
    temp=[]

    for i in range(k):
        temp.append(array[i])

    print temp

    for j in range(k,len(array)):
        tail=array[j]
        temp.append(tail)
        temp.pop(0)

        print(temp)




def main():

    array = [40, 8, 25, 24, 23, 109, 24, 9, 8, 11, 13, 42, 19]
    print(array)
    print("highest total with window of 4")
    slidingWindowHighestWindow(array,4)
    print("\n")
    print(array)
    print("lowest total with window of 4")
    slidingWindowLowestWindow(array,4)
    print("\n")
    print(array)
    print("windows with total higher then 50")
    howManyWindowsWithTotalGreaterThanVal(array,4,100)
    print("\n")
    print(array)
    print("print all sub array's size of 3")
    printAllSubArrays(array,3)
    #first i want to check the highest value in a sliding window

main()