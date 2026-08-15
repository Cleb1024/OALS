import re  # 정규표현식 사용
from collections import Counter  # 오류 코드별 발생 횟수 집계

log_path = "alert.log"  # 분석할 Alert Log 파일


# Alert Log 한 줄에서 ORA 코드와 메시지를 추출하는 함수
def parse_ora_line(line):
    # ORA- 뒤에 숫자 3~5자리와 ':' 이후 메시지를 각각 추출
    match = re.search(r"(ORA-\d{3,5}):\s*(.*)", line)

    # ORA 패턴이 발견된 경우 코드와 메시지를 반환
    if match:
        error_code = match.group(1)
        message = match.group(2)

        return error_code, message

    # ORA 패턴이 없는 줄은 None 반환
    return None


# ORA 코드별 발생 횟수를 저장할 Counter
error_counts = Counter()


# Alert Log 파일 열기
with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        # 앞뒤 공백과 줄바꿈 제거
        line = line.strip()

        # 현재 줄에서 ORA 정보 추출
        result = parse_ora_line(line)

        # ORA 오류가 발견된 경우 코드와 메시지를 각각 출력
        if result:
            error_code, message = result

            print(f"Error Code : {error_code}")
            print(f"Message    : {message}")
            print()

            # 해당 ORA 코드의 발생 횟수 1 증가
            error_counts[error_code] += 1


# ORA 코드별 발생 횟수 출력
print("=== ORA Error Summary ===")

for error_code, count in error_counts.items():
    print(f"{error_code} : {count}건")