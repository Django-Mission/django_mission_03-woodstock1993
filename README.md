# django_mission_03 _ LIKELION

## 과제 해석
- 진행정도를 표현하기 위한 상태필드 추가
- Inquiry List 속성 중 '상태정보'를 표시하기 위한 api 구성
- 관리자모드에서 User model의 특정 필드로 검색하기 위한 기능 추가
- admin.action을 통해 Inquiry 작성 시 email과 phone으로 답변을 받고자 하는 Inquiry의 해당 데이터 출력하는 기능 추가

## 구현

### 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/> <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

### 개발 기간
- 2022.04.27 - 2022.05.05

> ### ERD
> 
> ### API 명세
#### advertiser 관련
**광고주 조회** : GET /api/advertiser
<img src="./source/madup_api_advertiser_list.png" alt="api_advertiser_list"/>

- pk 값에 해당하는 광고주의 정보를 조회합니다.

### Step to run
```
$ python -m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py runserver
```
