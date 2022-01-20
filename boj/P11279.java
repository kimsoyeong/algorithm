package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class P11279 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		// 최대힙 -> 직접 구현해서도 풀어보기
		PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
		
		int max = 0;
		for(int i=0; i < N; i++) {
			int x = Integer.parseInt(br.readLine());
			if(max > x) {
				max = x;
			}
			if(x == 0) {
				if(heap.isEmpty()) {
					System.out.println(0);
				} else {
					System.out.println(heap.poll());	
				}
			} else {
				heap.add(x);
			}
		}
		
	}

}
