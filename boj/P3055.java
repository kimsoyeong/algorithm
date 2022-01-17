import java.util.ArrayList;
import java.util.Scanner;

class Node {
	int row;
	int col;
	char type;

	Node(int i, int j, char type){
		this.row = i;
		this.col = j;
		this.type = type;
	}
}

public class P3055 {

	static int R, C;
	static ArrayList<Node> q;
	
	static int[][] dp;
	static boolean foundAnswer;
	
	static final int[] DX = {-1, 1, 0, 0};
	static final int[] DY = {0, 0, -1, 1};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		R = sc.nextInt();
		C = sc.nextInt();

		char[][] map = new char[R][C];   // 지도
		dp = new int[R][C]; // 방문 여부) 방문x -> 0
		
		q = new ArrayList<>();
		
		int sx = 0, sy = 0; // start location
		
		for(int i=0; i < R; i++) {
			String line = sc.next();
			
			for(int j=0; j < C; j++) {
				map[i][j] = line.charAt(j);
				switch(map[i][j]) {
				case '*': // 물
					q.add(new Node(i,j, '*'));
					break;
				case 'S': // 고슴도치의 위치
					sy = i;
					sx = j;
					break;
				}
			}
		}
		
		q.add(new Node(sy, sx, 'S'));
		
		while(!q.isEmpty()) {
			// 1. 큐에서 꺼내옴 -> S, ., D, *
			Node p = q.remove(0);
			// 2. 목적지인가? -> D
			if(p.type == 'D') {
				System.out.println(dp[p.row][p.col]);
				foundAnswer = true;
				break;
			}
			// 3. 연결된 곳을 순회 -> 좌, 우, 위, 아래
			for(int i=0; i<4; i++) {
				int ty = p.row + DY[i];
				int tx = p.col + DX[i];
				// 4. 갈 수 있는 가? ( 공통 ) -> 맵을 벗어나지 않고
				if(0 <= ty && ty < R && 0 <= tx && tx < C) {
					if(p.type == '.' || p.type == 'S') { 
						// 4. 갈 수 있는 가? ( 고슴도치 ) -> 맵을 벗어나지 않고, . or D, 방문하지 않은 곳
						if((map[ty][tx] == '.' || map[ty][tx] == 'D') && dp[ty][tx] == 0) {
							// 5. 체크인 -> dp에 현재 + 1을 기록
							dp[ty][tx] = dp[p.row][p.col] + 1;
							// 6. 큐에 넣음
							q.add(new Node(ty, tx, map[ty][tx]));
						}
						
					} else if(p.type == '*') { 
						// 4. 갈 수 있는 가? ( 물 ) .
						if(map[ty][tx] == '.' || map[ty][tx] == 'S') {
							// 5. 체크인 -> 지도에 * 표기
							map[ty][tx] ='*';
							// 6. 큐에 넣음
							q.add(new Node(ty, tx, map[ty][tx]));
						}
						
					}
					
				}
			}
		}
		
		if(!foundAnswer) {
			System.out.println("KAKTUS");
		}
		
	}
}
