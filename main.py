import shark

money = shark.Economy(1328633162053582849, 853197257251618816)

print(money.money)
print(money.coin_name)

money = shark.EconomyItems(853197257251618816)

print(money.item)

score = shark.Score(1323780339285360660, 1335428061541437531)

print(score.score)