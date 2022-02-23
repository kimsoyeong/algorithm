import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9095 { // 1, 2, 3 더하기
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        int[] dp = new int[12]; // n의 최대값 = 11
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        while(T-- > 0){
            int n = Integer.parseInt(br.readLine());

            for(int i=4; i<n+1; i++){
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
            }

            System.out.println(dp[n]);
        }

    }
}
