package pta.collections;

import static pta.utils.Dummy.mayAlias;
import static pta.utils.Dummy.notAlias;

public class Array1-Mut00 {

  public static void main(String[] args) {

    Object [] array = new Object[] {};
    Object a = new Object();
    //Benchmark.alloc(1);
    Object b = new Object();
    array[0] = a;
    array[1] = b;
    Object c = array[1];
    
    notAlias(c,b);
    notAlias(a,array);
  }
}
