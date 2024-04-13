#Loyola, Reylene Grace A.
#IT3C
#WEEK 13 Merge Functions

def merge(place1, place2):
    place1.sort()
    place2.sort()
    mergeList = sorted(place1 + place2)
    return mergeList

def mergeAndSort(place1, place2):
    sortedList= merge(place1, place2)
    return sortedList

place1 = ["Manila", "Abra", "Camiguin", "Baguio"]
place2 = ["Zamboanga", "Tawi-Tawi", "Davao", "Palawan"]

result = mergeAndSort(place1, place2)
print("Merged and sorted list: {}".format(result))




