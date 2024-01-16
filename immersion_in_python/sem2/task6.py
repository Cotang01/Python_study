class ATMException(Exception):
    pass


class ATM:

    def __init__(self):
        self.working: bool = False
        self.money: float = 0
        self.withdraw_fee: float = 0.015
        self.withdraw_border: tuple[int, int] = (30, 600)
        self.operations_count = 0
        self.bonus = 0.03
        self.money_roof = 5_000_000
        self.luxury_tax = 0.1

    def _check_money_roof(self) -> None:
        if self.money > self.money_roof:
            self.money -= round(self.money * self.luxury_tax, 2)

    def _check_working_state(self) -> None:
        if not self.working:
            raise ATMException('Автомат не работает')

    def _check_bonus(self) -> None:
        self.operations_count += 1
        if self.operations_count % 3 == 0:
            self.money += round(self.money * self.bonus, 2)

    def _check_state_bonus_roof(self) -> None:
        self._check_working_state()
        self._check_bonus()
        self._check_money_roof()

    def start(self) -> None:
        self.working = True

    def exit(self) -> None:
        self.working = False

    def withdraw(self, amount) -> None:
        self._check_state_bonus_roof()
        if self.money < amount \
                or not self.withdraw_border[1] > amount \
                or not amount > self.withdraw_border[0]:
            raise ValueError('Нельзя снять такую сумму')
        self.money -= round(amount - amount * self.withdraw_fee, 2)
        self.operations_count += 1

    def deposit(self, amount: int) -> None:
        self._check_state_bonus_roof()
        self.money += amount


atm = ATM()
options = 'Доступные варианты:\n' \
                '1. Пополнение\n' \
                '2. Вывод\n' \
                '3. Включение\n' \
                '4. Выключение\n' \
                '5. Показать баланс\n'
print(options)


def main():
    while True:
        choice = input('Выберите действие: -> ')
        match choice:
            case '1':
                if not atm.working:
                    print('Включите аппарат')
                    main()
                to_deposit = int(input('Сколько пополнить? -> '))
                atm.deposit(to_deposit)
            case '2':
                if not atm.working:
                    print('Включите аппарат')
                    main()
                to_withdraw = int(input('Сколько вывести? -> '))
                atm.withdraw(to_withdraw)
            case '3':
                atm.start()
            case '4':
                atm.exit()
                break
            case '5':
                print(atm.money)
            case _:
                print(options)
                main()


main()
