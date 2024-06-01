class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n % 2 == 0) {
            // 짝수 일때
            for (int i = 1; i < n + 1; i++) {
                if ( i % 2 == 0) {
                    answer += i * i;
                }
            }
        }
        else {
            // 홀 수 일때
            for (int i = 1; i < n + 1; i++) {
                if ( i % 2 != 0) {
                    answer += i;
                }
            }
        }
        return answer;
    }
}