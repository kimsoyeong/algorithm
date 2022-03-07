import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2749 { // 피보나치 수3

    static long n;
    static long[] dp = new long[1500000];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Long.parseLong(br.readLine()); // int보다 큰 범위

        dp[0] = 0;
        dp[1] = 1;

        for(int i=2; i<1500000; i++){
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000;
        }

        System.out.println(dp[(int) (n % 1500000)]);
    }
}
