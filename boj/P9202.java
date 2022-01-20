package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9202 { // Boggle
	static int[] mx = {-1, 1, 0, 0, -1, 1, -1, 1};
	static int[] my = {0, 0, -1, 1, -1, -1, 1, 1};
	static int[] score = {0, 0, 0, 1, 1, 2, 3, 5, 11};

	static char[][] map;
	static boolean[][] visited;
	static String answer; // 현재 보글 보드에서 찾은 단어 중 가장 길이가 긴 단어
	static int sum; // 총 점수
	static int count; // 찾은 단어 수
	static int N; // 보글 보드 수
	static StringBuilder sb = new StringBuilder();
	static TrieNode root = new TrieNode();

	public static void main(String[] args) throws IOException { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int w = Integer.parseInt(br.readLine()); // 단어 사전에 들어있는 단어의 수

		for(int i=0; i<w; i++) {
			insertTrieNode(br.readLine());
		}

		br.readLine();
		N = Integer.parseInt(br.readLine());
		StringBuilder resultSb = new StringBuilder();
		for(int n = 0; n < N; n++) {
			map = new char[4][4];
			visited = new boolean[4][4];
			answer = "";
			sum = 0;
			count = 0;
			sb = new StringBuilder();
			
			for(int i=0; i<4; i++) {
				String in = br.readLine();
				for(int k=0; k<4; k++) {
					map[i][k] = in.charAt(k);
				}
			}
			br.readLine();
			for(int y=0; y < 4; y++) {
				for(int x = 0; x < 4; x++) {
					// 출발 가능 조건 -> root가 해당 child를 가지면
					if(root.hasChild(map[y][x])) {
						search(y, x, 1, root.getChild(map[y][x]));
					}
				}
			}
			// 결과 입력
			root.clearHit(); // 새로운 보글보드를 위해 hit를 clear해줘야 한다.
			resultSb.append(sum + " " + answer + " " + count + "\n");
		}

		System.out.println(resultSb.toString());
	}

	static void search(int y, int x, int length, TrieNode node) {
		// 1. 체크인
		visited[y][x] = true;
		sb.append(map[y][x]); // history 기억하기
		// 2. 목적지에 도달하였는가? -> isEnd, isHit
		if(node.isEnd && node.isHit == false) {
			node.isHit = true;
			sum += score[length]; // 단어 길이별 점수
			count++;
			String foundWord = sb.toString();
			if(compare(answer, foundWord) > 0) { 	// 새로 찾은 단어가 현재 정답 단어보다 더 길면
				answer = foundWord;					// 바꿔준다.
			}
		}
		// 3. 연결된 곳을 순회 -> 8방
		for(int i=0; i<8; i++) {
			int ty = y + my[i];
			int tx = x + mx[i];
			// 4. 가능한가? - map경계, 방문하지 않았는지, node가 해당 자식을 가지고 있는지
			if(0 <= ty && ty < 4 && 0 <= tx && tx < 4) { // map경계
				if(visited[ty][tx] == false && node.hasChild(map[ty][tx])) { // 방문여부, 자식여부: 갈 곳에 있는 애를 자식으로 가지는 지
					// 5. 간다
					search(ty, tx, length + 1, node.getChild(map[ty][tx])); // 현재 노드의 다음으로 찾을 노드를 준다.
				}
			}
		}
		// 6. 체크아웃
		visited[y][x] = false;
		sb.deleteCharAt(length - 1); // history 빼기
	}

	static int compare(String arg0, String arg1) {
		int result = Integer.compare(arg1.length(), arg0.length()); // 긴 거 찾아야함 -> 내림 차순
		if(result == 0) {
			return arg0.compareTo(arg1); // 알파벳 빠른 순
		} else {
			return result;			
		}
	}

	static void insertTrieNode(String word) {
		TrieNode current = root;
		for(int i=0; i < word.length(); i++) {
			if(current.hasChild(word.charAt(i)) == false){ // i번째 character가 없을 때 -> 새로 생성
				current.children[word.charAt(i) - 'A'] = new TrieNode();
			}
			// 자식으로 이동
			current = current.getChild(word.charAt(i));
		}
		current.isEnd = true;
	}

}

class TrieNode {
	TrieNode[] children = new TrieNode[26]; // 알파벳 대문자
	boolean isEnd;
	boolean isHit;

	boolean hasChild(char c) { // 실제 c라는 자식을 가지고 있는 지
		return children[c - 'A'] != null; // null이 아니란 것은 자식이 존재한다는 것
	}

	TrieNode getChild(char c) {
		return children[c - 'A'];
	}
	
	void clearHit() {
		isHit = false; // 본인 clear
		for(int i=0; i<children.length; i++) { // 자식 clear
			TrieNode child = children[i];
			if(child != null) {
				child.clearHit();
			}
		}
	}
}