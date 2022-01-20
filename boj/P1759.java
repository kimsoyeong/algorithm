package DAY01;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class P1759 {
	
	static int L, C;
	static String[] G;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		L = sc.nextInt();
		C = sc.nextInt();
		
		G = new String[C];
		int[] parent = new int[C];
		for(int i=0; i<C; i++) {
			G[i] = sc.next();
			parent[i] = -1; // parent: NIL
		}
		Arrays.sort(G); // 오름차순 정렬
		
		System.out.println(dfs(0, 0, ""));
	}
	
	public static boolean check(String str) {
		int j = 0;
		int m = 0;
		for(int i=0; i<str.length(); i++){
			char a = str.charAt(i);
			if (a== 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') {
				m += 1;
			} else {
				j += 1;
			}
		}
        
	    if(j >= 2 && m >=1) {
	    	return true;
	    } else {
	    	return false;
	    }
    }
	
	public static String dfs(int start, int depth, String p) {
		String result = "";
		
		if(depth == L) {
			if(check(p)) {
				return p+"\n";		
			}
		}
		
		for(int i=start; i<C; i++) {
			result += dfs(i+1, depth+1, p + G[i]);
		}
		
		return result;
	}
}
