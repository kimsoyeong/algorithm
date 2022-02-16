import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P16493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 남은 일 수
        int M = Integer.parseInt(st.nextToken()); // 챕터의 수

        int[] dp = new int[N+1];
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken()); // 각 챕터 당 읽는 데 소요되는 일 수
            int p = Integer.parseInt(st.nextToken()); // 페이지수

            for(int j=N; j>=d ;j--){
                dp[j] = Math.max(dp[j], dp[j - d] + p);
            }

        }

        System.out.println(dp[N]);

    }
}
