#-*-coding: utf8
#피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?
#대신짝수이면서 4백만 이하인 가장 큰 항은 얼마가 됩니까?
#* Recursion 재귀함수 를 이용해 볼 수 있겠습니까?
#로봇팔같은 기계에 리커션을 쓰면 안좋다.
import sys


def fibonacci(n):
    if 2==n:
        return 2
    elif 1 ==n:
        return 1
    elif 0 >= n:
        return 0
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def main():
    for i in range(1, 10 + 1):
        print ("Fibonacci(%d) = %d" %(i, fibonacci(i)))

    i = 11
    while True:
        f = fibonacci(i)
        if f > 4000000:
            print ("Fibonacci(%d) = %d" % (i, f))
            sys.exit(0)
        i += 1

if '__main__' == __name__:
    main()