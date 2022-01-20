package DAY02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2748 {

	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());

		long[] D = new long[N+1]; // 0 ~ N
		D[1] = 1;


		for(int i=2; i < N+1; i++) {
			D[i] = D[i-1] + D[i-2];				
		}

		System.out.println(D[N]);
	}

}
