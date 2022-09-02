sisters=('N','A','V','E','E','N')
#imaginary sisters
brothers=('G','O','U','D')
#imaginary brothers
siblings=sisters+brothers
#using the arthimatic operator
print(siblings)
print("NUMBER OF SIBLINGS:" + str(len(siblings)))
#used length to count the number of siblings
modify_list=list(siblings)
#As tuples are immutable we cannot add other elements.If you still want to add then you have to convert the tuple to list and convert it back to tuple.
print(modify_list)
modify_list.append("MOM")
#here adding mom to the list by using 'append',which adds only single item 
modify_list.append("DAD")
#here adding dad to the list
family_members=tuple(modify_list)
#here changed the list to tuple
print(family_members)