import pprint as pp

people={}
people['Ford']={'Name':'Ford Prefect',
                'Gender':'Male',
                'Occupation':'Researcher',
                'Home Planet':'Betelgeuse Seven'}

people['Arthur']={'Name':'Arthur Dent',
                'Gender':'Male',
                'Occupation':'Sandwich Maker',
                'Home Planet':'Earth'}

people['Trillian']={'Name':'Tricia McMillan',
                'Gender':'Female',
                'Occupation':'Mathematician',
                'Home Planet':'Earth'}

people['Robot']={'Name':'Marvin',
                'Gender':'Unknown',
                'Occupation':'Paranoid Android',
                'Home Planet':'Unknown'}

#pp.pprint(people)                  #use pprint to make the dictionary looks good
#print(people['Ford']['Name'])       #access a dictionary within a dictionary

names=[]

#exact just the names into a list from the dictionary within a dictionary
for p in people:
    data=people[p]['Name']
    names.append(data)

print(names)
