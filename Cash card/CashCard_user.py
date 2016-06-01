#-*- coding: utf8 -*-

#현금 카드 모듈을 불러 들임
import CashCard as CashCard_module


def chk_bal(message, account):
    """
    Print message and value
    :param message:
    :param account:
    :return:
    """
    print("%s : %d" % (message, account.check_balance()))


# 현금 카드 묘듈의 잔액 확인
chk_bal("CashCard_module 잔액 확인", CashCard_module)
#현금 카드에 10000원 입금
print "10000원 입금"
# ex09CahCard.py 모듈 안의 deposit() 함수를 호출
#ex09CashCard.py 모듈의 balance_won 값이 증가
CashCard_module.deposit(10000)

#ex09CahCard.py 모듈 안의 check() 함수를 호출
#ex09CashCard.py 모듈의 balance_won 값을 읽어 반환
chk_bal("입금 후 잔고 확인", CashCard_module)

# 또 다른 현금 카드를 만들 수있을까? 불러 들임
# noinnsepction PyPep3
import  CashCard as mySistersCard_module

chk_bal("CashCard_module 잔액 확인", CashCard_module)
chk_bal("mySisterCard_module 잔액 확인", mySistersCard_module)

#그러나 이런 식으로는 한장의 카드만 만들 수 있다.

print("CahsCard_module : %s" % CashCard_module)
print("mySistrersCard_module : %s" % mySistersCard_module)