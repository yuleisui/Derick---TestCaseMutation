package pta.special;

public class ThisPointer {
	static class A{void foo(){}}
	static class B extends A{void foo(){}}
	static A a;
	public static void main(String[] args) {
		a = new A();
		a = new B();
		a.foo();
	}
}
