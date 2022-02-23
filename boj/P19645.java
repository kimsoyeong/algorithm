import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P19645 { // 햄최몇?
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

//         햄최몇?
//         개수가 아니라 최대 효용이 중요하다!
//         N개의 햄버거 -> 나눠먹는다.
//         각자 획득 효용 = 먹은 햄버거들의 효용의 합
//         선배보다 높은 효용 X
//         막내 길원의 효용의 합의 최대값

        int n = Integer.parseInt(br.readLine());

        int[] ham = new int[n+1]; // 햄버거 효용
        int sum = 0;
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<n+1; i++){
            ham[i] = Integer.parseInt(st.nextToken());
            sum += ham[i];
        }

        boolean[][] dp = new boolean[sum+1][sum+1]; // dp[x][y]: 선배1 x효용일때 선배2가 y효용을 얻는 것이 가능한 지 여부
        dp[0][0] = true; // 0 >= 0
        for(int i=1; i<n+1; i++){
            for(int x=sum; x>=0; x--){
                for(int y=sum; y>=0; y--){
                    if(x - ham[i] >= 0)
                        dp[x][y] |= dp[x - ham[i]][y];
                    if(y - ham[i] >= 0)
                        dp[x][y] |= dp[x][y - ham[i]];
                }
            }
        }

        int answer = 0;
        for(int i=0; i<sum+1; i++){ // i: 첫째 효용
            for(int j=0; j <= i; j++){ // j: 둘째 효용 <= 첫째 효용
                int last = sum - i - j; // 막내 효용
                if(dp[i][j] && (j >= last)){ // 가능한 효용 && 둘째 > 막내
                    answer = Math.max(answer, last);
                }
            }
        }

        System.out.println(answer);
    }

}
