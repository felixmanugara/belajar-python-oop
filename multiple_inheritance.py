class Team():
    def setTeam(self,teamname):
        self.team = teamname
    
    def showTeam(self):
        print("team name: {}".format(self.team))

class Tipe():
    def setTipe(self,tipename):
        self.tipe = tipename
    
    def showTipe(self):
        print("Tipe Hero: {}\n".format(self.tipe))

class Hero(Team,Tipe):
    def __init__(self,name,health):
        self.name = name 
        self.health = health
        print("nama Hero: {}\nhealth: {}".format(self.name,self.health))


Kyojuro = Hero("Rengoku Kyojuro",100)
Kyojuro.setTeam("Pembasmi Iblis")
Kyojuro.setTipe("Hashira Api")
Kyojuro.showTeam()
Kyojuro.showTipe()

Akaza = Hero("Akaza",100)
Akaza.setTeam("Iblis bulan atas")
Akaza.setTipe("Iblis bulan atas III")
Akaza.showTeam()
Akaza.showTipe()