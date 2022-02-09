package Study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P4375 { // 1

	static String input;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		while((input = br.readLine()) != null) {
			int n = Integer.parseInt(input);
			int cnt = 1;
			
			int temp = 0;
			while(true) {				
				temp = (temp * 10 + 1) % n;
				
				if(temp == 0) {
					break;
				}
				
				cnt++;
			}
			
			System.out.println(cnt);
		}
	}

}
