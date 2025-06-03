from argparse import ArgumentError


class BankAccount:
    __bank_address = "1 Allenby St, Tel Aviv"

    def __init__(self, owner: str, balance: float):
        self.__owner = owner
        self.__balance = balance

    @classmethod
    def get_bank_address(cls) -> str:
        return cls.__bank_address

    @staticmethod
    def highest_balance(acc1: "BankAccount", acc2: "BankAccount", acc3: "BankAccount") -> float:
        return max(acc1.balance, acc2.balance, acc3.balance)

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount

    def is_rich(self) -> bool:
        return True if self.balance > 1000000 else False

    def __add__(self, other: "BankAccount, int, float"):
        if isinstance(other, BankAccount):
            if self.owner == other.owner:
                new_balance = self.balance + other.balance
                return BankAccount(self.owner, new_balance)
            else:
                return f"Joint: {self.owner} & {other.owner}"
        elif isinstance(other, (float, int)):
            return BankAccount(self.owner, self.balance + other)
        else:
            raise TypeError(f'BankAccount class does not support add for type {type(other)}')

    def __sub__(self, other: "BankAccount, int, float"):
        if isinstance(other, BankAccount):
            new_balance = self.balance - other.balance
            return BankAccount(self.owner, new_balance)
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance - other)
        else:
            raise TypeError(f'BankAccount class does not support sub for type {type(other)}')

    def __eq__(self, other: "BankAccount, int, float, tuple") -> bool:
        if isinstance(other, BankAccount):
            return (self.owner, self.balance) == (other.owner, other.balance)
        elif isinstance(other, (int, float)):
            return self.balance == float(other)
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.owner, self.balance) == other
        else:
            raise TypeError(f'BankAccount class does not support eq for type {type(other)}')

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        elif isinstance(other, (int, float)):
            return self.balance > other
        else:
            raise TypeError(f"Cannot compare BankAccount with type {type(other)}")

    def __ge__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.balance >= other.balance
        elif isinstance(other, (int, float)):
            return self.balance >= other
        else:
            raise TypeError(f"Cannot compare BankAccount with type {type(other)}")

    def __lt__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        elif isinstance(other, (int, float)):
            return self.balance < other
        else:
            raise TypeError(f"Cannot compare BankAccount with type {type(other)}")

    def __le__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.balance <= other.balance
        elif isinstance(other, (int, float)):
            return self.balance <= other
        else:
            raise TypeError(f"Cannot compare BankAccount with type {type(other)}")

    def __repr__(self) -> str:
        return f"BankAccount(owner='{self.owner}', balance={self.balance:.2f})"

    def __str__(self) -> str:
        return f"BankAccount of {self.owner} with balance {self.balance:.2f}"

    def __len__(self) -> int:
        return round(self.balance)

    def __getitem__(self, key):
        if key == "owner" or key == 0:
            return self.owner
        elif key == "balance" or key == 1:
            return self.balance
        else:
            raise ArgumentError(f"Unsupported key: {key}")

    def __iter__(self):
        yield self.owner
        yield self.balance

    # 7. Bonus Feature
    def freeze(self):
        self.__owner = "FROZEN"
        self.balance = 0.0


# --- Demo Code for BankAccount class ---

# Create accounts
acc1 = BankAccount("Alice", 800.0)
acc2 = BankAccount("Bob", 1200.0)
acc3 = BankAccount("Alice", 800.0)
acc4 = BankAccount("Charlie", 300.0)

# Test __repr__ / __str__
print("Accounts:")
print(acc1)
print(acc2)
print(acc3)

# Test __eq__ (same owner and balance)
print("\nEquality:")
print("acc1 == acc3:", acc1 == acc3)  # True
print("acc1 == acc2:", acc1 == acc2)  # False
print("acc1 == 800:", acc1 == 800)  # True
print("acc1 == ('Alice', 800):", acc1 == ("Alice", 800))  # True

# Test __ne__
print("\nInequality:")
print("acc1 != acc2:", acc1 != acc2)  # True

# Test __gt__ (based on balance)
print("\nGreater Than:")
print("acc2 > acc1:", acc2 > acc1)  # True
print("acc4 > acc1:", acc4 > acc1)  # False

# Test __lt__, __ge__, __le__
print("\nOther comparisons:")
print("acc1 < acc2:", acc1 < acc2)  # True
print("acc2 >= acc1:", acc2 >= acc1)  # True
print("acc4 <= acc1:", acc4 <= acc1)  # True

# Test __add__ (same owner)
print("\nAdd:")
acc5 = acc1 + acc3
print("acc5 (Alice + Alice):", acc5)

# Test __add__ (different owners)
acc6 = acc1 + acc2
print("acc6 (Alice + Bob):", acc6)

# Test __add__ with number
acc7 = acc1 + 200
print("acc1 + 200:", acc7)

# Test __sub__ with another account
acc8 = acc2 - acc1
print("acc2 - acc1:", acc8)

# Test __sub__ with number
acc9 = acc2 - 500
print("acc2 - 500:", acc9)

# Test __getitem__
print("\nGet item:")
print("acc1['owner']:", acc1['owner'])
print("acc1[1]:", acc1[1])  # balance

# Test __iter__
print("\nIterating acc1:")
for info in acc1:
    print(info)

# Test __len__
print("\nLength of acc1:", len(acc1))

# Test class method
print("\nBank address:", BankAccount.get_bank_address())

# Test static method
print("\nHighest balance:", BankAccount.highest_balance(acc1, acc2, acc4))
