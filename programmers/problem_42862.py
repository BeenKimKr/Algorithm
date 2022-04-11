def solution(n, lost, reserve):
    # 13, 14번 테스트 케이스
    lost.sort()
    reserve.sort()

    # 도난당했으나 여분의 체육복이 있는 학생들
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
    answer = n - len(lost)

    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
print(solution(5, [2, 4], [2, 4]) == 5)
print(solution(5, [2, 3], [3, 4]) == 4)
