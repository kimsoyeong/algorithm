import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class P10826 { // 피보나치 수 4

    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine()); // int보다 큰 범위

        BigInteger[] dp = new BigInteger[n + 2];
        dp[0] = BigInteger.ZERO; // long으로도 감당안되는 범위 -> 무한대를 다룰 수 있는 big integer 사용
        dp[1] = BigInteger.ONE;

        for(int i=2; i < n+1; i++){
            dp[i] = dp[i-2].add(dp[i-1]);
        }

        System.out.println(dp[n]);
    }
}
