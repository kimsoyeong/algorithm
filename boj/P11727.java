import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P11727 { // 2xn 타일링 2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        long[] dp = new long[1001];
        dp[1] = 1;
        dp[2] = 3;

        for(int i=3; i<1001; i++){
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-2]) % 10007;
        }

        System.out.println(dp[n]);

    }
}
