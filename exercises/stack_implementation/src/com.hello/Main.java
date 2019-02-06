//package com.hello;
public class Main{
	public static void main(String[] args) {
		System.out.println("Hello, World!");
		Stack stack = new Stack(3);
		stack.push(1);
		stack.push(2);
		stack.push(3);
		System.out.print(stack.pop());
		System.out.print(stack.pop());
		System.out.print(stack.pop());
		System.out.print(stack.isEmpty());
		System.out.print(stack.pop());
	}
}

