package DAY03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class P1927 {

	public static void main(String[] args) throws IOException {
//		Scanner sc = new Scanner(System.in);
//		int N = sc.nextInt();
//		PriorityQueue<Integer> heap = new PriorityQueue<>(); // 최소힙
//		int min = Integer.MAX_VALUE, minIdx = 0;
//		for(int i=0; i < N; i++) {
//			int tmp = sc.nextInt();
//			if(min > tmp) {
//				min = tmp;
//			}
//			if(tmp == 0) {
//				if(heap.isEmpty()) {
//					System.out.println(0);
//				} else {
//					System.out.println(heap.poll());	
//				}
//			} else {
//				heap.add(tmp);
//			}
//		}
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		MinHeap mh = new MinHeap();
		
		for(int i=0; i< N; i++) {
			int input = Integer.parseInt(br.readLine());
			if(input == 0) {
				System.out.println(mh.delete());
			} else {
				mh.insert(input);
			}
		}
	}

}

class MinHeap {
	List<Integer> list;
	// list와 arraylist간 시간복잡도 차이는 없다.
	// BUT get()호출이 미세하게 느릴 수 있지만 영향을 끼칠 정도는 아니다.
	
	public MinHeap() {
		list = new ArrayList<>();
		list.add(0);
	}
	
	public void insert(int val) {
		// 1. leaf 마지막에 삽입
		list.add(val);
		
		int current = list.size() - 1;
		int parent = current / 2;
		// 2. 부모와 비교 후 조건이 맞지 않으면 Swap		
		// 3. 조건이 만족되거나 root까지 반복
		while(true) {
			if(parent == 0 || list.get(parent) <= list.get(current)) {
				break;
			}
			int temp = list.get(parent);
			list.set(parent, list.get(current));
			list.set(current, temp);
			
			current = parent;
			parent =  current / 2;
		}
	}
	
	public int delete() {
		if(list.size() == 1) {
			return 0;
		}
		int top = list.get(1);		
		// 1. Root에 leaf 마지막 데이터 가져옴
		list.set(1, list.get(list.size() - 1));
		list.remove(list.size() - 1);
		
		// 2. 자식을 비교 후 조건이 맞지 않으면 swap
		// 3. 조건이 만족되거나 leaf까지 반복
		int currentPos = 1; // 현재 위치
		while(true) {
			int leftPos = currentPos * 2;
			int rightPos = currentPos * 2 + 1;
			
			// 자식 손자 유무 확인: 3-1. leaf 도착
			if(leftPos >= list.size()) {
				break;
			}
			
			// 왼쪽 자식 먼저 확인
			int minValue = list.get(leftPos);
			int minPos = leftPos;
			
			// 오른쪽 자식 확인
			// index 먼저 확인 && rightPos < minValue
			if(rightPos < list.size() && list.get(rightPos) < minValue) {
				minValue= list.get(rightPos); // minValue를 오른쪽걸로 갈아치움
				minPos = rightPos;
			}
			// Swap
			if(list.get(currentPos) > minValue) { // swap 해야한다.
				int temp = list.get(currentPos);
				// swap: min <-> current
				list.set(currentPos, minValue);
				list.set(minPos, temp);
				currentPos = minPos;
			} else { // swap 필요 X: 3-2. 조건 만족
				break; // 더 내려갈 필요없으니 탈출
			}
		}
		
		return top;
	}
}