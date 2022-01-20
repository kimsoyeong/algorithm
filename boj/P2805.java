package DAY02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2805 {

	static int N, M;
	static int[] trees;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		trees = new int[N];

		int max = 0;

		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			trees[i] = Integer.parseInt(st.nextToken());
			max = Math.max(trees[i], max);
		}

		long s = 0; // start
		long e = max; // end
		long mid = 0;
		long result = 0;
		while(true) {
			mid = (s + e) / 2;
			long sum = calc(mid);
			// sum == M -> 정답, 탈출
			if(sum == M) {
				result = mid;
				break;
			}
			// sum < M -> mid -> end
			else if (sum < M) {
				e = mid - 1;
			}
			// sum > M -> mid -> s, 정답 후보
			else {
				s = mid + 1;
				result = mid;
			}

			if (s > e) { // s가 e를 넘어섰을 때 -> 탈출
				break;
			}
		}

		System.out.println(result);

	}

	static long calc(long value) {
		long result = 0;
		for(int i=0; i< trees.length; i++) {
			int tree = trees[i];
			if(tree > value) {
				result += tree - value;
			}
		}
		return result;
	}
}
