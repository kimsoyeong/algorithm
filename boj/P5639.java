package DAY04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P5639 {
	
	// 후위 순회

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		BinaryTree2 bt = new BinaryTree2();
		
		while(true) {
			String tmp = br.readLine();
			if(tmp == null || tmp.equals("")) {
				break;
			}
			int x = Integer.parseInt(tmp);
			bt.add(x);
		}
		
		bt.postorder(bt.root);
	}

}

class Vertex {
	int data;
	Vertex left;
	Vertex right;
	
	Vertex(int data){
		this.data = data;
	}
}

class BinaryTree2 {
	Vertex root;
	
	void add(int data) {
		if(root == null) {
			this.root = new Vertex(data);
		}
		else {
			search(root, data);
		}
	}
	
	void search(Vertex root, int data) {
		if(root.data > data) { // 왼쪽 트리로
			if(root.left == null) {
				root.left = new Vertex(data);
			} else {
				search(root.left, data);
			}
		}
		else { // 오른쪽 트리로
			if(root.right == null) {
				root.right = new Vertex(data);
			} else {
				search(root.right, data);
			}
		}
	}
	
	void postorder(Vertex root) {
		if(root.left != null) postorder(root.left);
		if(root.right != null) postorder(root.right);
		System.out.println(root.data);
	}
}