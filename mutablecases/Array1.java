package pta.collections;

import static pta.utils.Dummy.mayAlias;
import static pta.utils.Dummy.notAlias;

/*
 * @testcase Array1
 * @description Array alias
 */
public class Array1 {

  public static void main(String[] args) {

    Object [] array = new Object[] {};
    Object a = new Object();
    //Benchmark.alloc(1);
    Object b = new Object();
    array[0] = a;
    array[1] = b;
    Object c = array[1];
    
    mayAlias(c,b);
    notAlias(a,array);

    /*Benchmark
        .test("c",
            "{allocId:1, mayAlias:[c,b], notMayAlias:[a,array], mustAlias:[c,b], notMustAlias:[a,array]}");*/
  }
}
