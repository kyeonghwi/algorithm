from datetime import datetime, timedelta

# 1. 현재 UTC+0 시간을 가져옵니다.
# (datetime.now() 대신 datetime.utcnow()를 사용하는 것이 더 명확합니다)
utc_now = datetime.utcnow()

# 2. 서울 시간(KST)은 UTC+9 이므로, 9시간을 더해줍니다.
kst_time = utc_now + timedelta(hours=9)

# 3. 9시간을 더한 시간에서 날짜 부분만 YYYY-MM-DD 형식으로 출력합니다.
print(kst_time.strftime('%Y-%m-%d'))
