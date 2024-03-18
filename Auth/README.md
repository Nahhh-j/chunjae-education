# 최초 1회
- 로그인을 할거에요(client)
	- ID, PW 서버에 입력 -> User table을 조회
	- 서버에서 ID, PW를 인식하고, 내가 Jun이라는 것을 확인
	- 새롭게 session table에 `jun이 로그인 했어` 정보를 기록.
		- session : key : value형태로 데이터가 저장이 되는데, 이것은 user table을 건드는 것 보다 효율적
		- session의 value에 `jun이 로그인 했어`

------
# 다음번 요청부터 계속 로그인 되어있는 상태
- 다음번 요청부터는 쭉- session에 저장되어 있는 `jun이 로그인 했어`을 확인하면 내가 jun이라는 것을 서버가 알 수 있게 됩니다.
	- jun에 대한 private 정보에 접근할 수 있게 되죠.

- 다음번 요청들에 대해서 session에 저장되어 있는 `jun이 로그인 했어`에 어떻게 접근하냐?
	- session key를 알고 있으면 해당 데이터에 접근이 가능.
	- session key : 요청마다 계속계속 서버에 전달이 되어야 합니다.
		- client에서 관리를 합니다.
		- cookie에 저장.