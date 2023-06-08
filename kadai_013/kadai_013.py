import math

# 第１引数に商品の金額、第２引数に消費税（10%）
def buy_item(price, tax):
    return math.floor(price*(1 + tax/100))
tax_inc_price = buy_item(105, 10)
print(f"税込価格: {tax_inc_price} 円")


def buy_item1(price, tax):
    tax_inc_price = math.floor(price*(1 + tax/100))
    print(f"税込価格: {tax_inc_price} 円")
buy_item1(105, 10)