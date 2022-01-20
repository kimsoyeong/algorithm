package DAY04;

import java.io.*;
import java.util.*;

public class P1991 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine()); // 이진트리 노드 개수
		
		BinaryTree bt = new BinaryTree();
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			char root = st.nextToken().charAt(0);
			char left = st.nextToken().charAt(0);
			char right = st.nextToken().charAt(0);
			
			bt.add(root, left, right);
		}
		
		bt.preorder(bt.root);
		System.out.println();
		bt.inorder(bt.root);
		System.out.println();
		bt.postorder(bt.root);
	}
}

class Node {
	char data;
	Node left;
	Node right;
	
	Node(char data){
		this.data = data;
	}
}

class BinaryTree {
	Node root;
	
	void add(char data, char left, char right) {
		if(root == null) { // 초기 root 삽입
			root = new Node(data);
			if(left != '.') root.left = new Node(left);
			if(right != '.') root.right = new Node(right);
		}
		else {
			search(root, data, left, right); // 자식(손자) 탐색해서 data가 일치하는 노드 찾기
		}
	}
	
	void search(Node root, char data, char left, char right) {
		if(root == null) 
			return; // 끝 도달 BUT 일치 노드 찾지 못함 -> 털츌
		else if(root.data == data) { // 찾았다! 여기서 자식 지정
			if(left != '.') root.left = new Node(left);
			if(right != '.') root.right = new Node(right);
		}
		else { // 못 찾았다? 더 깊게 탐색
			search(root.left, data,left, right); // 왼쪽 자식(손자) 탐색
			search(root.right, data, left, right); // 오른쪽 자식(손자) 탐색
		}
	}
	
	void preorder(Node root) {
		System.out.print(root.data);
		if(root.left != null) preorder(root.left);
		if(root.right != null) preorder(root.right);
	}
	
	void inorder(Node root) {
		if(root.left != null) inorder(root.left);
		System.out.print(root.data);
		if(root.right != null) inorder(root.right);
	}
	
	void postorder(Node root) {
		if(root.left != null) postorder(root.left);
		if(root.right != null) postorder(root.right);
		System.out.print(root.data);
	}
}