### 백준 16506. CPU
# n개의 각 줄에 어셈블리어 코드를 기계어 코드(이진수)로 번역하여 출력
import sys
input = sys.stdin.readline

# 명령어 개수 입력받기
n = int(input())

# 딕셔너리에 opcode 저장
opcode_machine = {'ADD' : '0000', 'SUB' : '0001', 'MOV': '0010', 'AND' : '0011', 
                  'OR' : '0100', 'NOT' : '0101', 'MULT' : '0110', 'LSFTL' : '0111', 
                  'LSFTR' : '1000', 'ASFTR' : '1001', 'RL' : '1010', 'RR' : '1011'}

for i in range(n):
    # 명령어 입력 받기
    input_data = input().split()
    machine_code = ''
    opcode = input_data[0]
    rd = input_data[1]
    ra = input_data[2]
    rb_or_c = input_data[3]

    # C로 끝나는 명령어인 경우
    if opcode[-1] == 'C':
        # C를 제외한 opcode(명령어) 사용
        machine_code += opcode_machine.get(opcode[:-1])
        # C로 끝나면 4번 비트가 1
        machine_code += '1'
    
    # C로 끝나지 않는 명령어인 경우
    else:
        # 명령어 그대로 사용
        machine_code += opcode_machine.get(opcode)
        # C로 끝나지 않는 경우 4번 비트가 0
        machine_code += '0'
    # 항상 0인 5번 비트
    machine_code += '0'

    # rd와 ra 비트를 3비트 이진수로 변환하여 추가
    # 해당 범위 [2:]인 이유 -> 이진수 변환시 접두사'0b'제외 위해
    # 문자열 변환 이유 -> 이진수 값 조작 및 관리 용이
    # 특정 비트 수 맞추며 최종 기계어 코드 형식 유지 가능
    machine_code += str(bin(int(rd)))[2:].zfill(3)
    machine_code += str(bin(int(ra)))[2:].zfill(3)

    # 4번 비트가 0이면 rb 사용
    if machine_code[4] == '0':
        # rb는 3비트
        machine_code += str(bin(int(rb_or_c)))[2:].zfill(3)
        # 마지막 비트는 항상 0
        machine_code += '0'
    
    # 4번 비트가 1이면 상수 #C 사용
    else:
        # 상수 #C는 4비트
        machine_code += str(bin(int(rb_or_c)))[2:].zfill(4)
    
    print(machine_code)