# django_mission_03 _ LIKELION

## 과제 해석
- 진행정도를 표현하기 위한 Inquiry 모델에 상태필드 추가
- 어드민페이지에 Inquiry List 중 (username, phone, email, inquiry_status)'를 표시하기 위한 list_display 추가
- 관리자모드에서 Inquiry에서 User model의 특정 필드(username, phone, email)로 검색하기 위한 기능 추가
- admin.action을 통해 Inquiry 작성 시 email과 phone으로 답변을 받고자 하는 Inquiry의 해당 데이터 출력하는 기능 추가

## 구현

### 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/> <img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&logo=PyCharm&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>

### 개발 기간
- 2022.04.27 - 2022.05.05

> ### ERD

![my](https://user-images.githubusercontent.com/67543838/166806638-0fb86cb7-78b0-426a-9e14-3afe42eafadd.png)

> ### API 명세
GET /inquiry/all

![image](https://user-images.githubusercontent.com/67543838/166804876-24924e1d-ff1a-4865-89d4-d68bfba73b83.png)


### Inquiry 관련
**Inquiry admin** : GET /127.0.0.1:8000/admin/support/inquiry/?q=admin

![image](https://user-images.githubusercontent.com/67543838/166804245-c0be1364-f2f9-4017-b9f8-241e88029cab.png)


### Step to run
```
$ python -m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py runserver
```
