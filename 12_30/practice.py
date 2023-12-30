# git 복습 : 레포지토리까지 만들기
# 1. git허브 사이트에 들어가기
# 2. create a new repository
# 3. public or private 선택
# 4. git clone "~~내 깃 레포 주소.git" (로컬로 가져오기)
# cd piro20
# ls 
# ls -al --> 이거 뭐였지
# 5. 숨겨진 폴더로 .git 파일이 생김.

# 깃 구조를 알아보자! 
# 6. 가져온 폴더 (working derectory) 

# Staging area : 임시저장
# git index폴더에 stage가 있다. -> 왜?? 무슨 관련이지..  
# git add <파일이름> : 해당 파일 무대로 올린다.
# git add . 현재 디렉토리부터 아래까지 다 무대로 올린다.
# git status : 무대에 아직 안올라간 애들은 red 올라가면 green

# stage에 올라간 것들을 끌어내릴때는...
# git reset <파일이름> : <특정애만 끌어내림>
# GIT HEAD 모두다 끌어내림
# EX. git reset <piro.py>

# Local repository 
# git Innit
# git add .
# git commit -m"~"
# git push 
# HEAD -> main 에서 HEAD가 뭐였지? 왜 main 브랜치를 가지고 있더라? 
# 현재branch가 main이 맞는가를 확인하자
# HEAD 위치 확신 명령어
# origin.HEAD. 같은건 뭐지? -> Originㅣ이란?
# Head가 가리키는 위치 옮기기 -> 어떻게 하더라?
# 돌아가고자 하는 커밋명을 복사해서 넣으면 git recet 
# 이전버전으로 돌리고 싶을때 사용하는 push

# 협업하려면 remote로 올려야함.
# remote repository ; 
#  각 임무 나누기 : 
# 회원 로그인 고객센터
# 결제 신용카드결제 포인트
# 상품 알뜰쇼핑 신상품 
# "기능단위"로 가져가서 개발을 해야 깃으로 협업하기 편리.

# git fetch가 뭐엿지?
# git pull origin main
# pull은 가져와서 내 로컬 디렉토리와 합쳐지는 것

# git checkout -b develop
# 현재 메인 브렌치 대신 develop 브랜치로 전환한다. 
# git branch 쳐보면 두개 다 나옴.
# checkout은 깃에 들어가겠다고 노크 똑똑
# git branchgit checkout -b feature/cart : feature/cart라는 브랜치가 만들어졌다. 

featrue/cart에서 무슨뜻이지?









