import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2073 { // 수도배관공사
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int D = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int[] L = new int[P+1]; // 파이프 길이
        int[] C = new int[P+1]; // 파이프 용량
        for(int i=1; i<P+1; i++){
            st = new StringTokenizer(br.readLine());
            L[i] = Integer.parseInt(st.nextToken());
            C[i] = Integer.parseInt(st.nextToken());
        }

        // 수도관
        // 용량: 최소 파이프 용량
        // 길이: 파이프 길이 총합
        // 길이가 D인 수도관을 만들 때 최대 수도관 용량을 구해라!

        int[] dp = new int[D+1];

        dp[0] = 100001;
        for(int i=1; i<P+1; i++){
            for(int j=D; j>=L[i]; j--){ // top-down
                dp[j] = Integer.max(dp[j], Integer.min(dp[j- L[i]], C[i]));
            }
        }

        System.out.println(dp[D]);

    }
}
