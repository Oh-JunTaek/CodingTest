from datetime import datetime

# 현재 날짜를 가져옵니다.
today = datetime.now()

# 날짜를 "YYYY-MM-DD" 형식으로 출력합니다.
print(today.strftime("%Y-%m-%d"))
