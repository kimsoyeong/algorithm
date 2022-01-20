package DAY02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2003 {

	static int N, M;
	static int[] nums;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		nums = new int[N+1];
		
		st = new StringTokenizer(br.readLine()); // 새로운 줄을 읽을 때 new 해줘야 한다.
		for(int i=0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int low = 0, high = 0, sum = nums[0], count = 0;
		
		while(true) {
			// sum == M -> 답 찾음 low ++
			if(sum == M) {
				count++;
				// sum -= nums[low]; // sum에서 low값 빼기
				// low++; // low 1 증가
				sum -= nums[low++]; // 한 줄로 구현
			}
			// sum > M -> low++
			else if(sum > M) {
				sum-= nums[low++];
			}
			// sum < M -> high++
			else {
				// high++;
				// sum += nums[high];
				sum += nums[++high]; // sum에 high + 1값 더하기
			}
			
			if(high == N) {
				break;
			}
		}
		
		System.out.println(count);

	}

}
