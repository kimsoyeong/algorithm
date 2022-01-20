package DAY02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1806 {

	static int N, S;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		
		int[] nums = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int low = 0, high = 0, sum = nums[0], len = Integer.MAX_VALUE;
		
		while(true) {
			if(sum >= S) { // sum >= M -> 답 찾음 low ++
				len = Math.min(len, (high - low + 1));
				sum -= nums[low++];
			}
			else { // sum < M -> high++
				sum += nums[++high]; // sum에 high + 1값 더하기
			}
			
			if(high == N) { // high 끝 도달
				break;
			}
		}
		
		if(len == Integer.MAX_VALUE) {
			System.out.println("0");
		} else {
			System.out.println(len);
		}
	}

}
