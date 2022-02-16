import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P23061 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 필수품 N개
        int M = Integer.parseInt(st.nextToken()); // 물건을 담을 가방 M -> 각 가방 Ki 무게 제한

        // 각 물건: 무게 W, 가치 V
        int[] W = new int[N+1];
        int[] V = new int[N+1];
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        // 각 가방의 제한 무게 K
        int[] K = new int[M+1];
        // 가장 무거운 가방의 무게 -> 이걸 구해놓으면 더 가벼운 가방들에 대해서도 한 번에 구해지므로 추가 연산이 줄어듦
        int maxbag = 0;
        for(int i=1; i<M+1; i++){
            K[i] = Integer.parseInt(br.readLine());
            maxbag = Math.max(K[i], maxbag);
        }

        long[] dp = new long[maxbag + 1];
        for (int i = 1; i <= N; i++) {
            for (int j = maxbag; j >= 0; j--) {
                if (j < W[i]) break;
                dp[j] = Math.max(dp[j], dp[j - W[i]] + V[i]);
            }
        }

        // 효율성 = (가방에 담긴 물건의 가치의 합) / (가방이 견딜 수 있는 최대 무게)
        // 가방 1개만 선택가능 -> 최적의 가방 번호 출력 (여러 개면 가장 작은 번호)
        int answer = 1;
        for(int i=2; i<=M; i++){
            // dp[answer] / K[answer] < dp[i] / K[i]
            // dp[answer] * K[i] < dp[i] * K[answer]
            if (dp[K[answer]] * K[i] < K[answer] * dp[K[i]]) {
                answer = i;
            }
        }
        System.out.println(answer);
    }
}
