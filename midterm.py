import random

myMoney = 200
result = ''
loop = True


class HorseRace:
    horses = ["charlie", "mac", "dee", "dennis"]

    def readySetGo(self):
        random.shuffle(self.horses)
        return

    def raceResults(self):
        print("\n[ Race Results ]")
        print(f'First place: {self.horses[0].capitalize()}')
        print(f'Second place: {self.horses[1].capitalize()}')
        print(f'Third place: {self.horses[2].capitalize()}')
        print(f'Fourth place: {self.horses[3].capitalize()}')

    def first(self):
        return self.horses[0]

    def second(self):
        return self.horses[1]

    def third(self):
        return self.horses[2]

    def fourth(self):
        return self.horses[3]


class BetList:
    bets = []

    def displayBetList(self):
        print("\n[ Your Previous Bets ]")
        if self.bets == []:
            print("No betting history.")
        else:
            for x in range(len(self.bets)):
                print(f'{self.bets[x]}')
        return self.bets


class Exacta:
    def makeExactaBet(self):
        global myMoney
        global result

        if myMoney < 10:
            print("  You don't have enough money to place this bet.")
        else:
            myMoney -= 10
            print("\nEnter the names of the two horses you'd like to bet on >> ")
            one = input("First horse: ")
            two = input("Second horse: ")
            one = one.lower()
            two = two.lower()

            if one and two not in ['mac', 'dennis', 'dee', 'charlie']:
                print(
                    "Those horses aren't registered with us. Make a new selection from the menu.")
            elif race.first() == one and race.second() == two:
                print(
                    "Winner, winner! Chicken dinner! You win $100. It has been added to your balance.")
                result = "won $100!"
                myMoney += 100
            else:
                print("Your horses were not winners. Try again!")
                result = "lost."

            bets.bets.append(
                f'You bet EXACTA on horses {one.capitalize()} and {two.capitalize()} and you {result}')

            print("A new race will now begin!")
            race.readySetGo()


class Exactabox:
    def makeExactaboxBet(self):
        global myMoney
        global result

        if myMoney < 5:
            print("  You don't have enough money to place this bet.")
        else:
            myMoney -= 5
            print("\nEnter the names of the two horses you'd like to bet on >> ")
            one = input("First horse: ")
            two = input("Second horse: ")
            one = one.lower()
            two = two.lower()

            if one and two not in ['mac', 'dennis', 'dee', 'charlie']:
                print(
                    "Those horses aren't registered with us. Make a new selection from the menu.")
            elif race.first() == one or race.first() == two and race.second() == one or race.second() == two:
                print(
                    "Winner, winner! Chicken dinner! You win $50. It has been added to your balance.")
                result = "won $50!"
                myMoney += 50
            else:
                print("Your horses were not winners. Try again!")
                result = "lost."

            bets.bets.append(
                f'You bet EXACTABOX on horses {one.capitalize()} and {two.capitalize()} and you {result}')

            print("A new race will now begin!")
            race.readySetGo()


class Trifecta:
    def makeTrifectaBet(self):
        global myMoney
        global result

        if myMoney < 25:
            print("  You don't have enough money to place this bet.")
        else:
            myMoney -= 25
            print("\nEnter the names of the two horses you'd like to bet on >> ")
            one = input("First horse: ")
            two = input("Second horse: ")
            three = input("Third horse: ")
            one = one.lower()
            two = two.lower()
            three = three.lower()

            if one and two not in ['mac', 'dennis', 'dee', 'charlie']:
                print(
                    "Those horses aren't registered with us. Make a new selection from the menu.")
            elif race.first() == one and race.second() == two and race.third() == three:
                print(
                    "Winner, winner! Chicken dinner! You win $200. It has been added to your balance.")
                result = "won $200!"
                myMoney += 200
            else:
                print("Your horses were not winners. Try again!")
                result = "lost."

            bets.bets.append(
                f'You bet TRIFECTA on horses {one.capitalize()}, {two.capitalize()}, and {three.capitalize()} and you {result}')

            print("A new race will now begin!")
            race.readySetGo()


class Trifectabox:
    def makeTrifectaboxBet(self):
        global myMoney
        global result

        if myMoney < 20:
            print("  You don't have enough money to place this bet.")
        else:
            myMoney -= 20
            print("\nEnter the names of the two horses you'd like to bet on >> ")
            one = input("First horse: ")
            two = input("Second horse: ")
            three = input("Third horse: ")
            one = one.lower()
            two = two.lower()
            three = three.lower()

            if one and two not in ['mac', 'dennis', 'dee', 'charlie']:
                print(
                    "Those horses aren't registered with us. Make a new selection from the menu.")
            elif race.first() == one or race.first() == two or race.first() == three and race.second() == one or race.second() == two or race.second() == three and race.third() == one or race.third() == two or race.third() == three:
                print(
                    "Winner, winner! Chicken dinner! You win $150. It has been added to your balance.")
                result = "won $150!"
                myMoney += 150
            else:
                print("Your horses were not winners. Try again!")
                result = "lost."

            bets.bets.append(
                f'You bet TRIFECTABOX on horses {one.capitalize()}, {two.capitalize()}, and {three.capitalize()} and you {result}')

            print("A new race will now begin!")
            race.readySetGo()


class Menu:
    def displayMenu(self):
        print("\nPlease make a selection from the menu below:")
        print("  1) Bet EXACTA - $10")
        print("  2) Bet EXACTABOX - $5")
        print("  3) Bet TRIFECTA - $25")
        print("  4) Bet TRIFECTABOX - $20")
        print("  5) View Race Results")
        print("  6) View Betting History")
        print("  7) View Cash Balance")
        print("  8) Reset Race")
        print("  9) Exit")


bets = BetList()
race = HorseRace()
menu = Menu()
exacta = Exacta()
exactabox = Exactabox()
trifecta = Trifecta()
trifectabox = Trifectabox()


class StartRace:
    global myMoney

    def startRace(self):
        print("\n[ Welcome to the Races! ]")
        print(
            f'Today\'s racers are Charlie, Mac, Dee, and Dennis!')

        menu.displayMenu()
        race.readySetGo()

        while loop:
            choice = int(input("\n  * Enter your selection: >> "))
            if choice not in range(1, 10):
                print("  Please choose a correct number from the selection above.")
            elif choice == 1:
                exacta.makeExactaBet()
            elif choice == 2:
                exactabox.makeExactaboxBet()
            elif choice == 3:
                trifecta.makeTrifectaBet()
            elif choice == 4:
                trifectabox.makeTrifectaboxBet()
            elif choice == 5:
                race.raceResults()
            elif choice == 6:
                bets.displayBetList()
            elif choice == 7:
                print("\n[ Your Cash Balance ]")
                print(f'You have ${myMoney} in your account.')
            elif choice == 8:
                print("\n[ Waiting for Next Race... ]")
                print("A new race will now begin!")
                race.readySetGo()
            elif choice == 9:
                print("\n[ Leaving the Races ]")
                print("See you next time!\n")
                break


playGame = StartRace()
playGame.startRace()
