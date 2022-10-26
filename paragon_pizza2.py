import math


def number_of_offenders(expected_balance, current_bal, offenders_bal):
    return math.ceil((expected_balance - current_bal) / offenders_bal)


if __name__ == '__main__':
    expected_price = 27000
    current_price = 4300
    offenders_price = 1000

print(f"The expected price of pizza is {expected_price}\nThe money at hand is {current_price}\nAll offenders are "
      f"Expected to pay {offenders_price} each")
print(f"Numbers of offenders is : {number_of_offenders(expected_price, current_price, offenders_price)}")

