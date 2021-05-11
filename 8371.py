# 문제
# 최근 몇 년 동안, 빌랜드의 어린이들은 거의 책을 읽지 않고 있다. 이것은 네덜란드 주민들의 맞춤법 지식에 부정적인 영향을 미친다. 
# 학교 교사들은 이 상황을 바꾸기 위해 최선을 다한다. 그들은 많은 다양한 시험과 대회를 조직한다. 목표는 학생들의 맞춤법 지식을 늘리는 것이다. 
# 그러나 이것은 상황을 크게 개선시키지 못한다. 많은 어린이들이 난독증 자격증을 가지고 있는데, 이것은 그들이 저지르는 철자 오류에 신경 쓰지 않게 해준다. 
# 교육부는 이 상황에 대응하기로 결정했다. 난독증 증명서의 모든 소유자는 그나 그가 정말로 난독증이라는 것을 증명해야 한다고 결정되었다. 
# 난독증에 의해 영향을 받는 Byteland에는 너무나 많은 어린이들이 있어서 검증 과정을 자동화해야 한다. 
# 모든 아이들은 컴퓨터에 있는 특별한 텍스트 세트를 다시 써야 할 것이다. 실수의 수는 학생이 난독증 환자인지 아닌지를 결정하는 것을 가능하게 할 것이다. 
# 교육부는 이 시험을 위한 검증 프로그램을 준비해주길 바란다.

# 다음과 같은 프로그램을 작성합니다.
# > 표준 입력에서 두 개의 텍스트를 읽습니다. 원본 텍스트와 학생이 다시 쓴 버전입니다.
# > 잘못 고쳐 쓴 글자의 수를 결정합니다.
# > 결과를 표준 출력에 기록합니다.

# 입력 
# 첫 번째 줄에는 원래 텍스트의 길이를 나타내는 정수 n(1 n n 100 100 000)이 있다. 
# 두 번째 행에는 원본 텍스트가 들어 있습니다. 
# 영어 알파벳의 작은 글자와 대문자로 구성되어 있습니다. 
# 세 번째 줄에는 학생이 다시 쓴 텍스트가 들어 있습니다. 또한 영어 알파벳의 작은 문자 및/또는 대문자로 구성됩니다.

import sys
n = int(sys.stdin.readline())
rawString = sys.stdin.readline()
writtenString = sys.stdin.readline()
cnt = 0
for i in range(n):
    if rawString[i] != writtenString[i]: cnt+=1
print(cnt)