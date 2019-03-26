line1 = [int(x) for x in input().split()]
N = line1[0]
K = line1[1]
totalpokemon = 0

pokemon = []
for x in range(N):
    pokemon.append([int(x) for x in input().split()])

def removechoice():    
    attack = [monster[0] for monster in pokemon]
    defend = [monster[1] for monster in pokemon]
    health = [monster[2] for monster in pokemon]
    
    choice = set()

    choice.add(attack.index(max(attack)))
    choice.add(defend.index(max(defend)))
    choice.add(health.index(max(health)))
    
    for index in sorted(choice, reverse = True):
        del pokemon[index]

    return len(choice)

for x in range(K):
    totalpokemon += removechoice()


print (totalpokemon)
        
    
    

