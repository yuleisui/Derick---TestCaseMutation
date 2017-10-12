package pta.collections;

import java.util.HashMap;


import static pta.utils.Dummy.mayAlias;
import static pta.utils.Dummy.notAlias;
/*
 * @testcase Map1
 * @description HashMap
 */
public class Map1 {

  public static void main(String[] args) {

    HashMap<String, Object> map = new HashMap<String, Object>();
    Object a = new Object();
    //Benchmark.alloc(1);
    Object b = new Object();
    map.put("first", a);
    map.put("second", b);
    Object c = map.get("second");
    mayAlias(c,b);
    notAlias(c,a);
    /*Benchmark.test("c",
        "{allocId:1, mayAlias:[c,b], notMayAlias:[a,map], mustAlias:[c,b], notMustAlias:[a,map]}");*/
  }
}
