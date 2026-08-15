import re  # 정규표현식 사용

log_path = "alert.log"  # 분석할 Alert Log 파일

# Alert Log 파일 열기
with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        # 앞뒤 공백과 줄바꿈 제거
        line = line.strip()

        # ORA- 뒤에 숫자 3~5자리가 있는 줄 탐지
        if re.search(r"ORA-\d{3,5}", line):
            print(f"[ORA ERROR] {line}")