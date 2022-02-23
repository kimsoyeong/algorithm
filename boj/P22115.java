import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P22115 { // 창영이와 커피
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // N개의 커피가 "하나씩" 준비
        // 각 커피 카페인 함유량 Ci
        // N개 커피 중 몇 개를 골라 -> (정확히) K만큼의 카페인을 섭취
        // 최소 몇 개의 커피를 마셔야 할까?

        int N = Integer.parseInt(st.nextToken()); // 커피 수
        int K = Integer.parseInt(st.nextToken()); // 섭취해야 하는 카페인 양

        int[] C = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for(int i=1; i<N+1; i++){
            C[i] = Integer.parseInt(st.nextToken()); // 커피 카페인 함유량
        }

        int[] dp = new int[K+1]; // index: 섭취 카페인 양
        Arrays.fill(dp, 10001); // 최소값을 찾기 위해 모든 값을 가능한 최대값으로 초기화
        dp[0] = 0; // 0 카페인 == 커피 0개
        for(int i=1; i<N+1; i++){
            for(int j=K; j>=C[i]; j--){
                dp[j] = Math.min(dp[j], dp[j-C[i]] + 1);
            }
        }

        System.out.println(dp[K] > 100 ? -1 : dp[K]);

    }
}
