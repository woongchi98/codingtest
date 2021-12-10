for part in participant: 
    for comp in completion:
        if part in completion:
            participant.remove(comp)

answer = participant[0]
#리스트를 사용 할 때는 크기를 조심해야한다.: 정수데이터는 int로 설정 하는 등
#용량초과로 실패
