package com.mulberrybeacon.sorting;

/**
 * Set of generic and common functions for sort algorithms.
 *
 * @author Eduardo Ferreira
 */
public class SortAlgorithm {

	/**
	 * Swaps a pair of elements.
	 *
	 * @param p1 First element of the pair
	 * @param p2 Second element of the pair
	 */
	protected static void swapElements(int[] list, final int index) {
		final int aux = list[index];
		list[index] = list[index + 1];
		list[index + 1] = aux;
	}
}
