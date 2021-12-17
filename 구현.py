'''
크기가 NxN인 지도.
여행가는 [L, R, U, D]에 따라서 움직인다.
근데 x좌표가 1일 때 L이 나오면 안움직인다. 즉 네모를 벗어나는 경우는 움직이지 않음.
최종 좌표를 구하라.

 - 입력조건
   첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <+ 100
   둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<= 이동횟수 <= 100
   
 - 출력조건
   첫째 줄에 여행가 A가 최종적으로 도차갛ㄹ 지점의 좌표를 공백으로 구분하여 출력한다.
'''

##첫번째 풀이
def solution(N, direction):
    now = [1,1]
    for i in direction:
        if (i == 'U'):
            if ((now[0] == 1)):
                pass
            else:
                now[0] -= 1
        elif (i == 'D'):
            if ((now[0] == N)):
                pass
            else:
                now[0] += 1
        if (i == 'L'):
            if ((now[1] == 1)):
                pass
            else:
                now[1] -= 1
        if (i == 'R'):
            if ((now[1] == N)):
                pass
            else:
                now[1] += 1

    answers = now
    return  answers
