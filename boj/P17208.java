import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P17208 { // 카우버거 알바생
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 최대 몇 개의 주문을 처리할 수 있을까?
        // 치즈버거 + 감자튀김

        int N = Integer.parseInt(st.nextToken()); // 주문의 수
        int M = Integer.parseInt(st.nextToken()); // 남은 치즈버거 수
        int K = Integer.parseInt(st.nextToken()); // 남은 감자튀김 수

        int[] x = new int[N+1];
        int[] y = new int[N+1];
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken()); // 치즈버거 요구 개수
            y[i] = Integer.parseInt(st.nextToken()); // 감자튀김 요구 개수
        }

        int[][] dp = new int[M+1][K+1]; // [burger][fries]
        for(int i=1; i<N+1; i++){ // 주문번호
            for(int j=M; j >= x[i]; j--){ // 치즈버거
                for(int k=K; k >= y[i]; k--){ // 감자튀김
                    dp[j][k] = Math.max(dp[j][k], dp[j - x[i]][k - y[i]] + 1);
                }
            }
        }

        System.out.println(dp[M][K]);
    }
}
