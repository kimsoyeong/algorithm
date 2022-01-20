package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class P10845 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		
		Queue s = new Queue();
		for(int i=0; i< N; i++) {
			st = new StringTokenizer(br.readLine());
			String cmd = st.nextToken();
			if(cmd.equals("push")) {
				int n = Integer.parseInt(st.nextToken());
				s.push(n);
			}
			else if(cmd.equals("pop")) {
				System.out.println(s.pop());
			}
			else if(cmd.equals("size")) {
				System.out.println(s.size());
			}
			else if(cmd.equals("empty")) {
				System.out.println(s.empty());
			}
			else if(cmd.equals("front")) {
				System.out.println(s.front());
			}
			else if(cmd.equals("back")) {
				System.out.println(s.back());
			}
			
		}
	}

}

class Queue {
	List<Integer> list;
	int size;
	
	
	Queue(){
		this.list = new ArrayList<>();
		size = 0;
	}
	
	void push(int n){
		list.add(n);
		size += 1;
	}
	
	int pop() {
		if(size < 1) return -1;
		int tmp = list.remove(0);
		size -= 1;
		return tmp;
	}
	
	int size() {
		return size;
	}
	
	int empty() {
		return size > 0 ? 0 : 1; // 비었으면 1, 아니면 0
	}
	
	int front() {
		if(size < 1) return -1;
		return list.get(0);
	}
	
	int back() {
		if(size < 1) return -1;
		return list.get(size-1);
	}
	
}