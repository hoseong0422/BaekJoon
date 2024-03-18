# [level 1] 삼총사 - 131705 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131128) 

### 성능 요약

시간 초과

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

Empty

### 문제 설명

<p>두 정수 <code>X</code>, <code>Y</code>의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). <code>X</code>, <code>Y</code>의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. <code>X</code>, <code>Y</code>의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.</p>

<p>예를 들어, <code>X</code> = 3403이고 <code>Y</code> = 13203이라면, <code>X</code>와 <code>Y</code>의 짝꿍은 <code>X</code>와 <code>Y</code>에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 <code>X</code> = 5525이고 <code>Y</code> = 1255이면 <code>X</code>와 <code>Y</code>의 짝꿍은 <code>X</code>와 <code>Y</code>에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(<code>X</code>에는 5가 3개, <code>Y</code>에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 <code>X</code>, <code>Y</code>가 주어졌을 때, <code>X</code>, <code>Y</code>의 짝꿍을 return하는 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>3 ≤ <code>X</code>, <code>Y</code>의 길이(자릿수) ≤ 3,000,000입니다.</li>
<li><code>X</code>, <code>Y</code>는 0으로 시작하지 않습니다.</li>
<li><code>X</code>, <code>Y</code>의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges