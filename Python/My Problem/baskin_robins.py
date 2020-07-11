from random import randint
win = 0
lose = 0

def baskin_robins():
    global win
    global lose
    global turn

    n = randint(31,50)
    k = randint(3,5)

    r = (n-1) % (k+1)
    i = 1


    print("""사용자와 컴퓨터 각 두 명은 번갈아가며 1부터 순서대로 숫자를 부르기 시작합니다.
    {}를 부르는 사람이 지고, 한 번에 {}개의 숫자를 부를 수 있습니다.
    순번을 결정하세요. 먼저 하고 싶으면 1번, 나중에 하고 싶으면 2번, 그만하고 싶으면 3번을 누르세요.
    """.format(n, k))
    while True:
        try:
            turn = int(input())
            break
        except:
            print("다시 입력하세요")

    if turn == 3:
        return


    while True:
        if turn == 1:

        # 사용자 턴
            while True:
                try:
                    count = int(input()) #사용자가 뽑을 숫자 개수 입력
                    print() 
                    break
                except:
                    print("다시 입력하세요")

            if 1 <= count <= k:
                print("사용자: ", end="")
                for m in range(count):
                    print(i, end=" ")
                    if i == n:
                        print("당신이 졌습니다ㅠㅠ")
                        lose += 1
                        return
                    i+=1



                print()
                turn = 2

            else:
                print("1부터", k, "까지의 수를 입력하세요.")



        else:    # 컴퓨터 턴
            if (i-1)%(k+1) == r:
                count = randint(1, k)

            else:
                count = (r-(i-1)%(k+1))%(k+1)

            print("컴퓨터: ", end="")

            for m in range(count): # count개를 print
                print(i, end=" ")
                if i == n:
                    print("당신이 이겼습니다!!")
                    win += 1
                    return
                i+=1

            print()

            turn = 1



while True:
    baskin_robins()
    win_rate = win / (win + lose) * 100
    print("승률: {}%".format(win_rate))
    print()

    if turn == 3:
        break

print("끝")

