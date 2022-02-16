import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14728 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        int[] dp = new int[T+1];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            int Ki = Integer.parseInt(st.nextToken());
            int Si = Integer.parseInt(st.nextToken());

            for(int j= T; j>=Ki; j--){
                dp[j] = Math.max(dp[j], dp[j - Ki] + Si);
            }

        }

        System.out.println(dp[T]);
    }
}
