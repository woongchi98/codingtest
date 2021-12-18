### https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    for i in participant: 
        if i in completion:
            participant.remove(i)
    return(participant)
# 이론상으로는 맞는것 같은데 계속 생각과는 다르게 실행된다. 왜 그럴까?
# 해결 못함
### 다시 보니까 둘 다 i로 해놔서 그렇네!

def solution(participant, completion):
    for part in participant: 
        for comp in completion:
            if part in completion:
                participant.remove(comp)

    answer = participant[0]
    return(answer)
# 리스트를 사용 할 때는 크기를 조심해야한다.: 정수데이터는 int로 설정 하는 등
# 용량초과로 실패
# 용량이 적게 드는 딕셔너리를 이용해야 한다.

def solution(participant, completion):
    data = dict()
    data['part'] = participant
    data['compl']= completion
## 이런식으로 dictionary를 만들려고 했으나, 딕셔너리는 중복이 안된다.
## 그래서 각 인원을 세는 dictionary를 생성한다.

def solution(participant, completion):
    answer = {}
    
    #participant를 카운트해주는 answer를 만든다.
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
    #값을 빼준다
    for j in completion:
        answer[j] -= 1
    #
    for k in answer:
        if answer[k] : 
            return k

# get 함수를 사용하였다
# dictionary.get(a,b) : key 'a'의 value 반환, 없으면 b를 반환
