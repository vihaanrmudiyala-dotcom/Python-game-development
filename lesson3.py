game={
    "Warrior":{
       'health':120,
       'weapon':'sword',
       'level':8,
       'coins':250
       },
       "wizard":{
          'health':80,
          "weapon":"magic staff",
          "level":10,
          'coins':400
        },
        "archer":{
           'health':100,
           'weapon':'bow'
           ,'level':7,
           'coins':250
           }
}
print('************All Charcters*************')
print(game)
print('\n*********Character Details********')
print("Warrior's Weapon:", game["Warrior"]['weapon'])
print("Wizard's Health:", game["wizard"]['health'])
print("Archer's level", game["archer"]['level'])
game['Warrior']['coins']=500
game['wizard']['health']=90
print('\n*********After Updating********')
print("Warrior's coins:", game["Warrior"]['coins'])
print("Wizard's Health:", game["wizard"]['health'])
game['Ninja']={
    'health':110,
    'weapon':"katana",
    'level':9,
    'coins':350
}
print('\n************After Adding A New Character*************')
print(game)
del game['archer']
print('\n************After Removing Archer*************')
print(game)
print('\n************Game Characters*************')
for character in game:
    print('\nCharacter:',character)
    for detail in game[character]:
     print(detail +':',game[character][detail])