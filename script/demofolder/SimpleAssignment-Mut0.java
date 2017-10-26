package pta.basic;

import static pta.utils.Dummy.mayAlias;

class SimpleAssignment-Mut0{
	public static void main(String[] argv){
		Object a=new Object();
		Object b=a;
		notAlias(a,b);
	}
}
