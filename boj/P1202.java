package DAY03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Jewel implements Comparable<Jewel>{
	int M; // 무게
	int V; // 가격
	Jewel(int m, int v){
		this.M = m;
		this.V = v;
	}
	
	@Override
	public int compareTo(Jewel o) {
		return Integer.compare(M, o.M); // 오름차순
	}
	
	public int getM() {
		return this.M;
	}
}

public class P1202 {

	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken()); // 보석 수
		int K = Integer.parseInt(st.nextToken()); // 가방 수
		// 1개 가방에 1개 보석만 담을 수 있다.

		// 현재 가방보다 무게가 같거나 작은 보석들을 우선순위 큐에 넣어둔다.
		// 가장 작은 무게의 가방에 그 무게보다 같거나 작은 보석들 중 가장 큰 가격의 보석을 담는다.
		Jewel[] jewels = new Jewel[N];
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			jewels[i] = new Jewel(m, v);
		}
		Arrays.sort(jewels); // 보석 무게 오름차순 정렬
		// Arrays.sort(jewels, Comparator.comparingInt(Jewel::getM));
		
		int[] C = new int[K]; // 각 가방 담을 수 있는 최대 무게들
		for(int i=0; i< K; i++) {
			int c = Integer.parseInt(br.readLine());
			C[i] = c;
		}
		Arrays.sort(C); // 가방 무게 오름차순 정렬
		
		// 보석 가격이 높은 값 기준 합(내림차순)
		PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

		long sum = 0; // 결과 범위는 long으로!
		int idx = 0;
		// 1. 남은 가방 중 가장 작은 가방 선택 <- 정렬
		for(int c: C) {
			// 2. 선택된 가방에 넣을 수 있는 남은 보석 중 가장 비싼 보석을 선택 <- 힙 사용
			while(idx < N) { // outofIndex 방지: 남은(아직 확인 안 한) 보석이 있는 동안 반복
				if(c >= jewels[idx].M) { // 선택된 가방에 들어갈 수 있는 모든 보석을 pq에 추가
					pq.add(jewels[idx++].V);
				} else {
					break;
				}
			}
			if(!pq.isEmpty()) {
				int currentMax = pq.poll(); // 최대값 반환 (reversed heap이라서)
				sum += Math.abs(currentMax);
			}
		}
		System.out.println(sum);

	}

}
