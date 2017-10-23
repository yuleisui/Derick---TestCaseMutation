package pta.basic;

import static pta.utils.Dummy.mayAlias;
import static pta.utils.Dummy.notAlias;

/*
 * @testcase Branching1
 * @description Condition. a and b alias on one path, not on the other
 */
public class Branching1 {

  public static void main(String[] args) {
  
  int i = 0;

  Object a = new Object();
  Object b = new Object();


    if (i < 0)
      a = b;

	mayAlias(a,b);
	notAlias(i,b);

    /*Benchmark.test("a",
        "{allocId:1, mayAlias:[a], notMayAlias:[i,b], mustAlias:[a], notMustAlias:[i,b]},"
            + "{allocId:2, mayAlias:[a,b], notMayAlias:[i], mustAlias:[a], notMustAlias:[i,b]}");
  	*/
  }
}
