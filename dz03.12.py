class CoffieMachine:
    curent_water = 1000
    min_water = 100
    quantiny_seed = 500
    min_quantiny_seed = 50
    __curent_garbage = 0
    __max_garbage = 10

    def garbage(self):
        self.__curent_garbage = 0

    def water_pull(self):
        self.curent_water = 1000

    def seed_pull(self):
        self.quantiny_seed = 500

    def clean_machine(self, trash):
        return self.__curent_garbage + trash >= self.__max_garbage

    def pull_water(self, water):
        return self.curent_water - water <= self.min_water

    def pull_seed(self, seed):
        return self.curent_water - seed <= self.min_quantiny_seed

    def amerikano(self):

        if self.pull_water(100):
            print('Нет воды')
            return
        if self.pull_seed(50):
            print('Нет зёрен')
            return
        if self.clean_machine(2):
            print('Почистить машину')
            return
        self.curent_water -= 100
        self.quantiny_seed -= 50
        self.__curent_garbage += 2
        print('Вот ваш Американо')

    def esperesso(self):
        if self.pull_water(100):
            print('Нет воды')
            return
        if self.pull_seed(50):
            print('Нет зёрен')
            return
        if self.clean_machine(1):
            print('Почистить машину')
            return
        self.curent_water -= 100
        self.quantiny_seed -= 25
        self.__curent_garbage += 2
        print('Вот ваш Еспрессо')




# coffe = CoffieMachine()

class MilkCoffee(CoffieMachine):
    curent_milk = 900
    min_milk = 200

    def milk_pull(self):
        self.curent_milk = 900

    def check_milk(self, milk):
        return self.curent_milk - milk <= self.min_milk


    def latte(self):
        if self.pull_water(100):
            print('Нет воды')
            return
        if self.pull_seed(50):
            print('Нет зёрен')
            return
        if self.clean_machine(3):
            print('Почистить машину')
            return
        if self.check_milk(200):
            print('Надо долить молоко')
            return
        self.curent_water -= 100
        self.quantiny_seed -= 50
        self._CoffieMachine__curent_garbage += 2
        self.curent_milk -= 200
        print('Вот ваш Латте')

    def capuchino(self):
        if self.pull_water(100):
            print('Нет воды')
            return
        if self.pull_seed(50):
            print('Нет зёрен')
            return
        if self.clean_machine(3):
            print('Почистить машину')
            return
        if self.check_milk(300):
            print('Надо долить молоко')
            return
        self.curent_water -= 100
        self.quantiny_seed -= 50
        self._CoffieMachine__curent_garbage += 2
        self.curent_milk -= 300
        print('Вот ваш Капучинно')

class AlkoCoffee(MilkCoffee):
    curent_Alko = 200
    min_Alko = 50

    def Nado_v_magaz(self):
        self.curent_Alko = 200

    def check_Alko(self, konyak):
        return self.curent_Alko - konyak <= self.min_Alko


    def Coffe_s_konyakom(self):
        if self.pull_water(100):
            print('Нет воды')
            return
        if self.pull_seed(50):
            print('Нет зёрен')
            return
        if self.clean_machine(3):
            print('Почистить машину')
            return
        if self.check_Alko(50):
            print('Надо в магаз')
            return
        self.curent_water -= 100
        self.quantiny_seed -= 50
        self._CoffieMachine__curent_garbage += 2
        self.curent_Alko -= 50

        print('Хорошего вчера')
#
# coffe = CoffieMachine()
# americ = coffe.amerikano()
# esp = coffe.esperesso()

# milkcof = MilkCoffee()
# # lat = milkcof.latte()
# # capuch = milkcof.capuchino()
#
alkoCoffee = AlkoCoffee()
coffee = alkoCoffee.Coffe_s_konyakom()
# # for coffee in range(2):
# # print(esp)