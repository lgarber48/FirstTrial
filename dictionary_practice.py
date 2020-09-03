#for dictionary, first part is key and second part is value
#notice use of curly braces
person3={'Name': 'Ford Prefect',
'Gender':'Male',
'Occupation':'Researcher',
'Home Planet':'Betelgeuse Seven'}

person3['Age']=33   #add to dictionary
person3['Gender']='Male'

#print(person3['Age'])    #use the key to reference the desired value

vowels=['a','e','i','o','u']

word=input('Provide a word').lower()    #takes input makes it all lowercase

found={}   #creates starting dictionary, must initialize values is using a counter 

 
for letter in word: #iterate through all the letters in the word, NOTE: can use in or not in 
    if letter in vowels:    #note: for boolean variables, must be True and False not true and false
        found.setdefault(letter,0)
        #found[letter]=0    #initilize values in dictionary
        found[letter]+=1   #instead of ++ Python uses += or -=, for this line, use "letter" instead of each letter

for k,v in found.items():   #items allows you to iterate over a dictionary row by row
    print(k,'was found',v,'time(s).')
