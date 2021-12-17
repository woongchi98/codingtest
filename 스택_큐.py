# 스택 ( 선입후출 )
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()

stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# 큐 (선입 선출)
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

queue.append(1)
queue.append(4)
queue.popleft()

print(queue)

queue.reverse()
print(queue)


# 재귀 함수 (자기 자신을 호출함)
def recursive_fun():
  print('무한')
  recursive_fun()
 
#종료조건 > 스택구조임
def recursive_fun(i):
    if i == 100:
        return
    print(i, '번째에서', i+1, '번째 재귀함수 호출')
    recursive_fun(i+1)
    print(i, '번째 재귀함수 종료')
# 1에서 2호출
# 2에서 3호출
# ~~~
# 99에서 100 호출
# 99번째 함수 종료
# 98번째 함수 종료
# ~~~
# 1번째 함수 종료


#재귀함수 예시
def factorial(i):
    if i <= 1:
        return 1
    return(i*factorial(i-1))
#반복문
def factorial(i):
    answer = 1
    for j in range(i):
        answer = answer * (j+1)
    return answer
  
#재귀함수가 더 간결하게 표현 할 수 있다.
#재귀함수 = 점화식 / 종료조건 필수!!!!!!!
