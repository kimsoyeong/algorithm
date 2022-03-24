import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class P2164 { // 카드2
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        // (위)1 ~ N(아래) 번호 카드
        // 가장 위 카드를 바닥에 버린다.
        // 다음 위 카드를 가장 아래 카드 밑으로 옮긴다.

        // 예) N = 4 -> 카드 1 2 3 4
        // (1 버림) 2 3 4
        // (2 가장 아래로) 3 4 2
        // --------------------
        // (3 버림) 4 2
        // (4 가장 아래로) 2 4
        // --------------------
        // (2 버림) 4
        // 남은 카드 = 4

        Queue<Integer> cards = new LinkedList<>();
        for(int i=1; i<=N; i++){
            cards.offer(i);
        }

        while(cards.size() > 1){
            cards.poll();
            cards.offer(cards.poll());
        }

        System.out.println(cards.poll());

    }
}
