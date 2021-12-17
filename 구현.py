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
   
   '''
   return 값이 리스트 형식이다
   리스트 형식을 어떻게 바꾸지?
   (now[0], now[1]) 이렇게 출력하면 되겠다.
   '''
   
   
#풀이 2
def solution(N, direction):
    x, y = 1, 1

    move_typaes = ['L','R','D','U']
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    nx = 0
    ny = 0
    
    for i in direction :
        for j in range(len(move_types)):
            if i == move_types[j] :
                nx = x + dx[j]
                ny = y + dy[j]
            
        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue
            
        x, y = nx, ny
    return (x,y)

   
'''
여기서 continue 와 pass의 차이를 꺠달음.
pass : 시행할 것이 없다는 의미
continue : 반복문 처음으로 돌아감.
위 예제에서는 nx나 ny가 범위를 벗어나면 다음 시행을 하는것.
'''
