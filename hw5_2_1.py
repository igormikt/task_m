has_money = True
friend_pay = True
is_sick = True

if (has_money or friend_pay) and not is_sick:
    print("Идём в кино")
else:
    print("Не идём в кино")