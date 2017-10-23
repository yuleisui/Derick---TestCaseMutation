package pta.collections;

import java.util.LinkedList;

import static pta.utils.Dummy.mayAlias;
import static pta.utils.Dummy.notAlias;

/*
 * @testcase List2
 * @description LinkedList
 */
public class List2 {

  public static void main(String[] args) {

    LinkedList<Object> list = new LinkedList<Object>();
    Object a = new Object();
    //Benchmark.alloc(1);
    Object b = new A();
    list.add(a);
    list.add(b);
    Object c = list.get(1);

    mayAlias(c,b);
    notAlias(a,list);
    /*Benchmark
        .test("b",
            "{allocId:1, mayAlias:[c,b], notMayAlias:[a,list], mustAlias:[c,b], notMustAlias:[a,list]}");*/
  }
}
