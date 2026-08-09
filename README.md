# OALS

Oracle Alert Log Study

Oracle Database의 Alert Log를 Python으로 읽고 분석하면서, DBA 관점에서 주요 이벤트와 오류를 탐지하고 분류하는 도구를 만드는 프로젝트입니다.

## 목표

Alert Log를 단순히 출력하는 것에서 시작하여 다음 기능을 단계적으로 구현합니다.

* ORA 오류 탐지
* 주요 Database Event 분류
* 이벤트 중요도 분류
* 오류 발생 전후 Context 확인
* Alert Log 분석 결과 요약

## 현재 구현

### Alert Log Reader

`alert_reader.py`를 이용하여 `alert.log` 파일을 한 줄씩 읽어 출력합니다.

실행:

`python alert_reader.py`

## 개발 계획

1. Alert Log Reader
2. ORA Error Detector
3. Event Classifier
4. Severity Classifier
5. Error Context
6. Analysis Summary

## 개발 방식

기능별 Branch에서 작업한 뒤 Pull Request를 통해 `main`에 반영합니다.

### Branch 예시

* `feature/log-reader`
* `feature/ora-detector`
* `feature/event-classifier`
* `docs/readme`

## 스터디 진행 기록

### 2026-08-09

* Git / GitHub 개발 환경 구성
* OALS Repository 생성
* Python 및 Jupyter 실행 테스트
* `feature/log-reader` 브랜치 생성
* Alert Log 기본 Reader 구현
* 첫 Pull Request 및 Merge
