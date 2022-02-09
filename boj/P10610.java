package Study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class P10610 { // 30

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String N = br.readLine();
		
		Integer[] nums = new Integer[N.length()];

		int sum = 0;
		for(int i=0; i<N.length(); i++) {
			nums[i] = Character.getNumericValue(N.charAt(i));
			sum += nums[i];
		}
		
		// 30의 배수인가?
		// 1. 3의 배수인가: 모든 수 합이 3
		// 2. 0이 있는가
		if(sum % 3 == 0 && N.contains("0")) {
			Arrays.sort(nums, Collections.reverseOrder());
			for(int i=0; i<nums.length; i++) {
				System.out.print(nums[i]);
			}
		}
		else System.out.println(-1);
		
	}
}
