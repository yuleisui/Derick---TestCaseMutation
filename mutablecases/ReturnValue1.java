package pta.basic;

import static pta.utils.Dummy.mayAlias;

  
public class ReturnValue1 {



  public static Object id(A x) {
    return x;
  }

  public static void main(String[] args) {

    Object a = new Object();
    Object b = id(a);
    mayAlias(a,b);
  }
}
