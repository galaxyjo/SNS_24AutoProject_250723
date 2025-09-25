# 📘 SNS 24AutoProject 사용자 매뉴얼

## 개요
이 매뉴얼은 SNS 자동화 시스템의 구성 및 사용 방법을 설명합니다.

## 디렉토리 구조
- launcher/: 실행 시작점
- modules/: 주요 기능 모듈
- scripts/: 보조 스크립트
- tests/: 테스트 코드
- db/: 데이터베이스 파일

## 사용 방법
1. `.env` 설정
2. PowerShell에서 `python launcher/main.py` 실행
3. 로그는 `db/account_log.db`에 저장됨

## 자동화 관련 스크립트
- `generate_manuals.py`: 이 매뉴얼을 생성
- `inspect_users_table.py`: 사용자 테이블 상태 확인
- `generate_log_summary.py`: 로그 요약 파일 생성

## 마지막 생성일
- 📅 SNS_24AutoProject_250723
