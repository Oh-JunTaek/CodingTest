# 입력된 괄호 문자열을 받습니다.
dish = input()

# 초기 높이는 첫 그릇이 바닥에 놓인 상태로 10cm입니다.
height = 10

# 첫 번째 그릇을 기준으로 다음 그릇들과 비교합니다.
for i in range(1, len(dish)):
    if dish[i] == dish[i - 1]:
        # 같은 방향으로 쌓이면 5cm 증가
        height += 5
    else:
        # 반대 방향으로 쌓이면 10cm 증가
        height += 10

# 최종 계산된 높이를 출력합니다.
print(height)