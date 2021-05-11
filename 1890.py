import sys
import pprint as pp

def data_in():
    # N = int(sys.stdin.readline())
    list = [['2', '3', '3', '1'],
            ['1', '2', '1', '3'],
            ['1', '2', '3', '1'],
            ['3', '1', '1', '0']]
    # for _ in range(N):list.append(sys.stdin.readline().split())
    return 4,list
        
def solution(N,list):
    pp.pprint(list)
    num = int(list[0][0])
    for i in range(N):
        print("{}: {}".format(list[i],len(list[i])))

    # print(list[0+num][0])
    # print(list[0][0+num])

if __name__ == '__main__':
    N ,list = data_in()
    solution(N,list)