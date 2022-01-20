package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;

public class P4358 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		HashMap<String, Double> hm = new HashMap<>();
		double N = 0.;
		while(true) {
			String input = br.readLine();
			if(input == null || input.equals("")) break;
			
			if(!hm.containsKey(input)) {
				hm.put(input, 1.);
			} else {
				hm.put(input, hm.get(input) + 1);
			}
			
			N++;
		}
		
		Object[] trees = hm.keySet().toArray();
		Arrays.sort(trees);
		
		for(Object tree: trees) {
			String tr = tree.toString();
			System.out.println(tr + " " + String.format("%.4f", hm.get(tr)/N * 100.));
		}

	}

}
