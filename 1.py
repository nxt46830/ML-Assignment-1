import math
ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
#sort() function is  used to sort ages.
print("sorted list",ages)
#the above line is used to print the sorted list of ages.
print("The Min age is" , ages[0], "and The Max age is",ages[-1])
sum_of_min_age_max_age=ages[0]+(ages[-1])
print("Sum of min age and max age ",sum_of_min_age_max_age)
ages.append(ages[0]+ages[-1])
#append function is used to add a item to the given list.
mid = len(ages) // 2
#length function is used to find the length of the given list
sum_age=0
if len(ages)%2==0:
    median=(ages[mid]+ages[~mid])/2
#if function is used to check a given condition is valid or not.If the condition is valid loop execute
else:
    median=ages[mid]
for age in ages:
    sum_age=sum_age+age
average =round(sum_age/len(ages),2)
#round function is used to round-up a number
print("Median",median)
print("Average",average)
print("range of ages list is",ages[-1]-ages[0])