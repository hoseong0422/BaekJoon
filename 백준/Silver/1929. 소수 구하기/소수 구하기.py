import sys

def sieve_range(m, n):
    # 0~n까지 소수 여부 테이블 (True=소수 가정)
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0: is_prime[0] = 0
    if n >= 1: is_prime[1] = 0

    # i*i가 n을 넘기 전까지만 확인
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if is_prime[i]:
            # i의 배수 제거는 i*i부터 시작 (그 이전 배수는 이미 지워짐)
            step_start = i * i
            is_prime[step_start:n+1:i] = b"\x00" * ((n - step_start)//i + 1)

    # m~n 구간의 소수만 출력
    out = []
    for x in range(m, n + 1):
        if is_prime[x]:
            out.append(str(x))
    return "\n".join(out)

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n = map(int, input().split())
    print(sieve_range(m, n))