from abc import ABC, abstractmethod
from typing import override, Optional, Dict


class ITransfer(ABC):
    @abstractmethod
    def transfer(self, amount: float, to_account: 'BankAccount') -> bool:
        pass


class IVerifyCreditCard(ABC):
    @abstractmethod
    def verify_credit_card(self, card_number: str) -> bool:
        pass


class IVerifyPayPal(ABC):
    @abstractmethod
    def verify_paypal_email(self, email: str) -> bool:
        pass


class BankAccount(ITransfer, IVerifyCreditCard, IVerifyPayPal):
    def __init__(self, id: str, balance: float, credit_card_number: Optional[str], paypal_email: Optional[str]):
        self.__id = id
        self.__balance = balance
        self.__credit_card_number = credit_card_number
        self.__paypal_email = paypal_email

    @property
    def id(self):
        return self.__id

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def credit_card_number(self):
        return self.__credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, credit_card_number):
        self.__credit_card_number = credit_card_number

    @property
    def paypal_email(self):
        return self.__paypal_email

    @paypal_email.setter
    def paypal_email(self, paypal_email):
        self.__paypal_email = paypal_email

    @override
    def transfer(self, amount: float, to_account: 'BankAccount') -> bool:
        if self.balance >= amount:
            self.balance -= amount
            to_account.balance += amount
            print("Transfer completed successfully!")
            return True
        print("Balance is insufficient!")
        return False

    @override
    def verify_credit_card(self, card_number: str) -> bool:
        return self.credit_card_number == card_number

    @override
    def verify_paypal_email(self, email: str) -> bool:
        return self.paypal_email == email

    def __str__(self):
        return (f"Account ID: {self.id}, Balance: {self.balance}, "
                f"Card: {self.credit_card_number}, PayPal: {self.paypal_email}")


class Payment(ABC):
    def __init__(self, amount: float, from_account_id: str, to_account_id: str):
        self.__amount = amount
        self.__from_account_id = from_account_id
        self.__to_account_id = to_account_id

    @property
    def amount(self):
        return self.__amount

    @property
    def from_account_id(self):
        return self.__from_account_id

    @property
    def to_account_id(self):
        return self.__to_account_id

    @abstractmethod
    def process(self, accounts: Dict[str, BankAccount]) -> bool:
        pass


class CreditCardPayment(Payment):
    def __init__(self, amount: float, from_account_id: str, to_account_id: str, card_number: str):
        super().__init__(amount, from_account_id, to_account_id)
        self.__card_number = card_number

    @property
    def card_number(self):
        return self.__card_number

    @override
    def process(self, accounts: Dict[str, BankAccount]) -> bool:
        from_acc = accounts.get(self.from_account_id)
        to_acc = accounts.get(self.to_account_id)

        if not isinstance(from_acc, IVerifyCreditCard):
            print("From account does not support credit card verification.")
            return False

        if from_acc.verify_credit_card(self.card_number):
            return from_acc.transfer(self.amount, to_acc)

        print("Credit card verification failed.")
        return False


class PayPalPayment(Payment):
    def __init__(self, amount: float, from_account_id: str, to_account_id: str, email: str):
        super().__init__(amount, from_account_id, to_account_id)
        self.__email = email

    @property
    def email(self):
        return self.__email

    @override
    def process(self, accounts: Dict[str, BankAccount]) -> bool:
        from_acc = accounts.get(self.from_account_id)
        to_acc = accounts.get(self.to_account_id)

        if not isinstance(from_acc, IVerifyPayPal):
            print("From account does not support PayPal verification.")
            return False

        if from_acc.verify_paypal_email(self.email):
            return from_acc.transfer(self.amount, to_acc)

        print("PayPal verification failed.")
        return False


def main():
    accounts = {
        "A001": BankAccount("A001", 1000.0, credit_card_number="1234567890123456", paypal_email="user1@example.com"),
        "A002": BankAccount("A002", 500.0, credit_card_number="1111222233334444", paypal_email="user2@example.com")
    }

    payments = [
        CreditCardPayment(200.0, "A001", "A002", card_number="1234567890123456"),  # valid
        PayPalPayment(300.0, "A001", "A002", email="wrong@example.com"),  # invalid email
        CreditCardPayment(900.0, "A002", "A001", card_number="1111222233334444")  # insufficient funds
    ]

    for payment in payments:
        print(payment.process(accounts))
        print("-" * 40)

    for acc in accounts.values():
        print(acc)


if __name__ == "__main__":
    main()
