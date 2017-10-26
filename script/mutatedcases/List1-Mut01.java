package pta.collections;

import java.util.ArrayList;

import static pta.utils.Dummy.mayAlias;
import static pta.utils.Dummy.notAlias;

/*
 * @testcase List1
 * @description ArrayList
 */
public class List1-Mut01 {

  public static void main(String[] args) {

    ArrayList<Object> list = new ArrayList<Object>();
    Object a = new Object();
    //Benchmark.alloc(1);
    Object b = new Object();
    list.add(a);
    list.add(b);
    Object c = list.get(1);
    
    notAlias(c,b);
    mayAlias(a,list);
    /*
    Benchmark
        .test("b",
            "{allocId:1, mayAlias:[c,b], notMayAlias:[a,list], mustAlias:[c,b], notMustAlias:[a,list]}");*/
  }
}
