import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P1463 { // 1로 만들기
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());


        int[] dp = new int[N+1]; // dp[i]: 숫자가 i일때 1을 만드는 연산 횟수의 최소

        // dp[n] = dp[n/3] + 1
        // dp[n] = dp[n/2] + 1
        // dp[n] = dp[n-1] + 1
        for(int X=2; X<N+1; X++){
            dp[X] = dp[X-1] + 1;
            if(X%2 == 0) dp[X] = Math.min(dp[X], dp[X/2] + 1);
            if(X%3 == 0) dp[X] = Math.min(dp[X], dp[X/3] + 1);
        }

        System.out.println(dp[N]);
    }
}
