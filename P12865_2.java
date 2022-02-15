import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P12865_2 {

    static int[] V, W;
    static Integer[][] bag;

    public static void main(String[] args) throws IOException { // 평범한 배낭
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력
        int N = Integer.parseInt(st.nextToken()); // 물품 수
        int K = Integer.parseInt(st.nextToken()); // 배낭 최대 무게

        V = new int[N + 1];
        W = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken()); // 무게
            V[i] = Integer.parseInt(st.nextToken()); // 가치

        }

        bag = new Integer[N + 1][K + 1];

        System.out.println(knapsack(N, K));

    }

    static int knapsack(int i, int k){
        if(i<0) return 0;

        if(bag[i][k] == null){
            if(W[i] > k){
                bag[i][k] = knapsack(i - 1, k);
            }
            else {
                bag[i][k] = Integer.max(knapsack(i-1, k), knapsack(i-1, k-W[i]) + V[i]);
            }
        }

        return bag[i][k];
    }
}
