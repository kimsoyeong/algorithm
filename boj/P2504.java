package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class P2504 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();

		Stack<Character> stack = new Stack<>();

		int answer = 0;
		int sum = 1;

		// (): 2
		// []: 3

		for(int i=0; i<input.length(); i++) {
			char c = input.charAt(i);				

			if(c=='(') {
				stack.add(c);
				sum *= 2;
			}
			else if(c=='[')	{
				stack.add(c);
				sum *= 3;
			}
			else if(c==')') {
				if(stack.isEmpty() || stack.peek() != '(') { // 올바르지 못한 경우
					answer = 0;
					break;
				}
				if(input.charAt(i - 1) == '(')	answer += sum;
				stack.pop();
				sum /= 2;
			}
			else if(c==']') {
				if(stack.isEmpty() || stack.peek() != '[') { // 올바르지 못한 경우
					answer = 0;
					break;
				}
				if(input.charAt(i - 1) == '[')	answer += sum;
				stack.pop();
				sum /= 3;
			}
		}
		
		if(!stack.isEmpty()) answer = 0;
		System.out.println(answer);
	}
}
