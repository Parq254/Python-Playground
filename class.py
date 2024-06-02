class Animal:
    def movement(self):
        type_of_movement = input("On Two's or Four's: ").capitalize()
        if type_of_movement == 'Two':
            print('Human')
        else:
            print('Creature')


class Human(Animal):
    def talk(self):
        print('Hello')


Chris = Human()
Chris.movement()
