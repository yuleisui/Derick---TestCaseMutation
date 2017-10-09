package pta.utils;

public class Dummy {
	// dummy methods for testee
	public static void call(Object... o) {
		// to prevent the compiler to prune the Object
	}

	public static <O> O getConst(O constant) {
		// to prevent the compiler to prune the Object containing only constant
		return constant;
	}
	
	public static void mayAlias(Object a, Object b) {
		// to be detected by Analyzer
	}

	public static void notAlias(Object a, Object b) {
		// to be detected by Analyzer
	}
}
