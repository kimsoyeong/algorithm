import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P3067 {

    static int[] coins;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스의 수

        while(T-- > 0) {
            int N = Integer.parseInt(br.readLine()); // 동전의 가지 수
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(br.readLine()); // 만들어야 할 금액

            coins = new int[N];
            for(int i=0; i<N; i++) // 동전 종류
                coins[i] = Integer.parseInt(st.nextToken());

            dp = new int[M+1]; // dp[money]: money원을 만드는 방법의 수
            dp[0] = 1; // 0원을 만드는 방법의 수
            for(int coin: coins){
                for(int money=1; money <= M; money++){ // money원 만드는 방법
                    if(money - coin >= 0){
                        dp[money] += dp[money - coin];
                        // money원을 만드는 방법의 수
                        // = money-coin원을 만드는 방법의 수 + 현재 coin을 제외하고 money원을 만드는 방법의 수
                    }
                }
            }
            System.out.println(dp[M]);
        }

    }
}
