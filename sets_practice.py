#in sets duplicates are forbidden

#vowels=['a','e','i','o','u'] list
#vowels={'a','e','i','o','u'} set
vowels=set('aeiou') #create set

word=input('Provide a word').lower()   #takes input makes it all lowercase

u=vowels.union(set(word))              #combines 2 sets to create new set containing both 
ulist=sorted(list(u))                  #easy way to sort to list in a certain order - must flip to list
#print(ulist)

d=vowels.difference(set(word))         #returns what is contained in set 1 (vowels) but not set 2 (word)
#print(d)

i=vowels.intersection(set(word))       #returns what is contained in both set 1 and set 2
ilist=sorted(list(i))

for vowels in ilist:
    print(vowels)

