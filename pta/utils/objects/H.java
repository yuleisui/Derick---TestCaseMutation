package pta.utils.objects;

public class H implements I {
	// G and H implement I

	A a;

	public A foo(A a) {
		this.a = a;
		return a;
	}
}
