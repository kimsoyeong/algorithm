import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P4781 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 구매한 사탕의 칼로리가 더 큰 사람이 내기에서 이긴다.
        // 사탕 개수는 제한이 없다.
        // 사탕은 쪼갤 수 없다.


        // 가장 큰 칼로리의 합을 만들자!
        int n;
        int m;
        while(true){
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken()); // 사탕 종류의 수
            m = Integer.parseInt(st.nextToken().replace(".",""));
            // m: 상근이가 가진 돈의 양 -> 항상 소수점 둘째짜리까지 입력됨
            if(n == 0 && m == 0) break;

            // n개 줄: c - 사탕 칼로리, p - 사탕 가격
            int[] c = new int[n];
            int[] p = new int[n];
            int[] dp = new int[m + 1]; // m=8.00 -> dp[801]

            for(int i=0; i<n; i++){
                st = new StringTokenizer(br.readLine());
                c[i] = Integer.parseInt(st.nextToken());
                p[i] = Integer.parseInt(st.nextToken().replace(".",""));
            }

            for(int i=0; i<n; i++){
                int price = p[i];
                for(int j=1; j<m+1; j++){
                    if(price <= j) {
                        dp[j] = Integer.max(dp[j], dp[j - price] + c[i]);
                    }
                }
            }

            System.out.println(dp[m]);
        }
    }
}
