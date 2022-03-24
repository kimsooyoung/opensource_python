Chapter 4
Python Advanced(4) - 나만의 패키지 만들기(3) - PyPI 배포
Keyword - PyPI, build, package deploy

일전 작성한 패키지를 누군가 사용한다면 이렇게 코드를 작성할 것이다.

```python
# py_ad_4_3 : 완성된 패키지 임포트
from py_ad_4_3 import GifConverter as gfc

# 클래스 생성
c = gfc("./project/images/*.png", './project/image_out/result.gif', (500,240))

# 실행
c.convert_gif()
```

패키지 배포 순서 - PyPI

1. https://pypi.org/ 회원가입

pip install 했을 때 당겨오는 곳이 여기이다. 가입 후 로그인할 때는 username 을 사용함에 유의

2. 프로젝트 구조 확인 

upload_package 안에 강의자가 이미 파일들을 만들어 두었다. 각각이 뭔지는 따로 설명이 없으므로 찾아보자. 

https://eu4ng.tistory.com/37 

3. 패키지 이름에 해당하는 폴더와 __init__.py 생성

현재는 pygifconvt를 이름으로 하였으며 이 이름은 pypi의 것과 겹치면 안된다.

그런 다음 기존 코드를 converter.py라는 파일에 복붙함 

4. 프로젝트 Root 필수 파일 작성
    - gitignore : 보통 pypi에 올리고 또 깃허브에도 올린다. 이를 위한 파일
    - README.md
	- setup.py : 중요한 것들 (name, 버전, author, install_requires(이거 해야 자동설치됨), keywords (검색 시 검색어), classifiers는 다 의미가 있다. 참고 - https://pypi.org/classifiers/)
	- setup.cfg(optional) : 불필요한 파일 배제 등 
	- LICENSE : 현재 MIT 라이센스 사용 https://m.blog.naver.com/occidere/220850682345 / 
	- MANIFEST.in : 파이썬과 관련 없는 파일들을 가져와야 하는지 등을 명시, 장고 파일 참고 - https://github.com/django/django/blob/main/MANIFEST.in

보통 위 6개는 다 있다.

5. pip install setuptools wheel 설치 후 빌드업 -> 설치판 생성
    - > 설치1 : python -m pip install  --upgrade setuptools wheel 
    ㄴ 가상환경 실행 시 이거 추천
	->  설치2 : python -m pip install  --user --upgrade setuptools wheel
    ㄴ 전역으로 하기 위해  --user 사용
	- > 빌드 : python setup.py sdist bdist_wheel
    ㄴ 배포판을 만드는 작업, setup.py가 있는 위치에서 실행해야 함

wheel : 파일 압축 해서 cpython 같은 실행 파일로 만들어주는 역할
setuptools : 압축 짐을 싸준다고...

=> 위 작업을 모두 하면 dist, bulid 폴더가 생긴다.

6. PyPI 배포
    - > 설치 : pip install twine
	- > 업로드 : python -m twine upload dist/*
7. 설치 확인(pip install pygifconvt)
    - > from pygifconvt import GifConverter as Alias

pypi에서 twine을 사용해서 업로드하기를 권장하고 있음.

다시 배포하고 싶은 경우, 
setup.py에서 버전 수정 후 다시 빌드
dist 폴더에 다시 새로운 버전이 생기며 새로운 버전 업로드 하면 됨 

15:50

```python
```

```python
```