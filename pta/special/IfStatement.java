package pta.special;

import static pta.utils.Dummy.notAlias;
import static pta.utils.Dummy.call;

public class IfStatement {
	static class A{
		Object f;
	}
	public static void main(String[] args) {
		A v1 = new A();
		v1.f= new Object();
		A v2 = new A();
		A v = selectA(v1,v2);
		v.f=v.f;
		notAlias(v1.f, v2.f);
	}
	private static A selectA(A v1, A v2) {
		A ret=null;
		Object f=null;
		for(int i=0;i<2;i++){
			ret = v1;
			f=ret.f;
			if(i==0)break;
			ret = v2;
			f=ret.f;
		}
		call(f);
		return ret;
	}
}
