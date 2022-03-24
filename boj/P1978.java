import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;
        for(int i=0; i<N; i++){
            int num = Integer.parseInt(st.nextToken());
            boolean isPrime = true;

            if(num <= 1) isPrime = false;
            else {
                for(int j=2; j*j<=num; j++){ // j: 2 ~ root(num)
                    if(num % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
            }

            answer = isPrime == true ? answer+1 : answer;
        }

        System.out.println(answer);
    }
}
