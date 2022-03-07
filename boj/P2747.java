import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2747 { // 피보나치 수

    static int n;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        dp = new int[n+2];
        System.out.println(fibo(n));
    }

    static int fibo(int n){
        if(n==0) return 0;
        if(n==1) return 1;
        if(dp[n] > 0) return dp[n];
        dp[n] = fibo(n-1) + fibo(n-2);
        return dp[n];
    }
}
