line1 = [int(x) for x in raw_input().split()]


N = line1[0]
K = line1[1]
gym = []

class pokemon:
    def __init__(self,number,attack,defence,health):
        self.number = number
        self.attack = attack
        self.defence = defence
        self.health = health
        
    def describe(self):
        stats = [self.number,self.attack,self.defence,self.health]
        return stats

'''for sorting'''
def takeattack(elem):
    return elem.attack

def takehealth(elem):
    return elem.health

def takedefence(elem):
    return elem.defence

Chosen = set()

'''list of pokemon'''
for a in range(N):
    stats = [int(x) for x in raw_input().split()]
    gym.append(pokemon(a,stats[0],stats[1],stats[2]))


gym.sort(key=takeattack, reverse = True)
for x in range(K):
    Chosen.add(gym[x].number)
    
gym.sort(key=takehealth, reverse = True)
for x in range(K):
    Chosen.add(gym[x].number)
    
gym.sort(key=takedefence, reverse = True)
for x in range(K):
    Chosen.add(gym[x].number)
    
print(len(Chosen))

