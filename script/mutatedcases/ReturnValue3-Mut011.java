package pta.basic;

import static pta.utils.Dummy.notAlias;

/*
 * @testcase ReturnValue3
 * @description Alias to a return value from a static method
 */
public class ReturnValue3-Mut011 {

  class A {
    Object f = new Object();
    public A() {}
    public A(B b) {
		this.f = b;
	}
  }
  
  public static Object id(A x) {
    A y = new A();
    y.f = new Object();
    return y;
  }

  public static void main(String[] args) {
    A a = new A();
    A b = id(a);
    Object x = b.f;
    Object y = a.f;
    notAlias(a,b);
    mayAlias(a,y);
    mayAlias(b,y);
  }
}
