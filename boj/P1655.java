package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

// day3 문제 but day4에 도전
public class P1655 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringBuilder sb = new StringBuilder(); // stringbuilder 사용하지 않고 매번 출력하면 시간초과 발생
		
		PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder());
		PriorityQueue<Integer> min = new PriorityQueue<>();
		// [------max------]<=[------min------] 형태로 유지
		// max힙의 값은 모두 min힙 값보다 작아햐한다.
		for(int i =0; i<N; i++) {
			int x = Integer.parseInt(br.readLine());

			// 최대 힙의 peek -> 중간값!
			if(i % 2 == 0) { // 최대힙 크기 == 최소힙 크기 -> 최대힙에 추가 ) 결국 i로 확인 가능
			// if(max.size() == min.size()) 와 같음
				max.add(x);
			} else {
				min.add(x);
			}
			
			if(!min.isEmpty() &&
					max.peek() > min.peek()) { // max 가장 큰 값이 min의 가장 작은 값보다 크다면 바꿔준다.
				min.add(max.poll()); // priorityqueue.poll() (첫번째:우선순위가 가장 높은 값 반환 제거) -> 최대힙의 최대값
				max.add(min.poll()); // 최소힙의 최소값
			}
			sb.append(max.peek()).append("\n");
		}		
		System.out.println(sb);
	}

}
