import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P12865 {
    public static void main(String[] args) throws IOException { // 평범한 배낭
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 입력
        int N = Integer.parseInt(st.nextToken()); // 물품 수
        int K = Integer.parseInt(st.nextToken()); // 배낭 최대 무게

        int[] V = new int[N+1];
        int[] W = new int[N+1];
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(br.readLine());
            W[i] = Integer.parseInt(st.nextToken()); // 무게
            V[i] = Integer.parseInt(st.nextToken()); // 가치

        }

        int[][] bag = new int[N+1][K+1];

        for(int i=1; i<N+1; i++){  // 몇 번 물품까지 탐색
            for(int weight=1; weight<K+1; weight++){ // index j는 곧 현재 채우는 가방의 무게 (최대 무게)
                if(W[i] > weight) bag[i][weight] = bag[i-1][weight];
                else if(W[i] <= weight){
                    bag[i][weight] = Integer.max(V[i] + bag[i-1][weight - W[i]], bag[i-1][weight]);
                }
            }
        }

        // 가치의 최대값 출력
        System.out.println(bag[N][K]);
    }
}
