package Study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2014 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int K = Integer.parseInt(st.nextToken()); // K개의 소수
		int N = Integer.parseInt(st.nextToken());
		
		int[] primes = new int[K];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<K; i++) { // K개의 소수가 오름차순으로
			primes[i] = Integer.parseInt(st.nextToken());
		}
		
		int answer = 0;
		// 소수의 곱을 (어딘가)에 넣는다.
		// (어딘가)에는 값이 중복되면 안된다. -> Set? HashMap?
		// (어딘가).length >= N이면 더이상 삽입X
		// (어딘가)의 top을 출력

		System.out.println(answer);
	}

}
