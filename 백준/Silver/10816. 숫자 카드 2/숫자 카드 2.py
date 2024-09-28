N = int(input())
N_num = list(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))

# 1. N_num에 있는 숫자들의 등장 횟수를 기록할 딕셔너리 생성
count_dict = {}

for num in N_num:
    if num in count_dict:
        count_dict[num] += 1  # 이미 존재하면 값을 1 증가
    else:
        count_dict[num] = 1  # 처음 등장하는 숫자는 1로 초기화

# 2. M_num에 있는 각 숫자가 N_num에 몇 번 있는지 출력
for num in M_num:
    # 딕셔너리에서 num의 개수를 찾아 출력, 없으면 0 출력
    print(count_dict.get(num, 0), end=' ')