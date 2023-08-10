# Release Note

## Team : Storage Apps
## Project : RYZEN

### [2023-08-10]
1. 접수 일자 : 2023.07.10
2. 요청자 : OOO
3. 요청 종류  : BUG 수정
4. 요청 사항 :
    > 4-1) func init 부분에서 error 현상 발생 수정 원함
    > 4-2) H/W 관련 이슈 해결
    > 4-3) PCI 정보를 받아오고 싶음
5. 원인 :
    > 5-1) init 함수 수정
    > 5-2) module에서 data 값 read/write 작업 수행 후 해결
    > 5-3) PCI Info 받아오는 함수 추가
6. 수정 사항 :
    > 6-1) GPIO Init 추가
    > >     - Add GPIO Init
    > 6-2) Hardwired Revison 추가
    > >     - Add Hardwired Revison
    > 6-3) Implement getPciSwitchInfo 추가
    > >     - Implement getPciSwitchInfo
