package pta.basic;

import static pta.utils.Dummy.mayAlias;

import pta.utils.objects.A;
/*
 * @testcase ReturnValue2
 * @description Alias to a return value from a static method
 */
public class ReturnValue2 {

  public ReturnValue2() {}

  public Object id(A x) {
    return x;
  }

  public static void main(String[] args) {

    Object a = new Object();
    ReturnValue2 x = new ReturnValue2();
    Object b = x.id(a);
    mayAlias(a,b);
  }
}
