package com.mulberrybeacon.sorting;

/**
 * Several possible implementations of the Merge Sort algorithm.
 * 
 * @author Eduardo Ferreira
 */
public class MergeSort {

	/**
	 * Top-down version of Merge Sort.
	 *
	 * @param list List of numbers
	 */
	public static int[] mergeSort(int[] list) {

		// Checks if the list is already sorted
		if (list.length <= 1) {
			return list;
		}

		// Lists to store the left and right sides of the list
		final int leftSize = list.length / 2;
		int[] left = new int[leftSize];
		int[] right = new int[list.length - leftSize];

		// Stores the left half of the list
		for (int i = 0; i < leftSize; i++) {
			left[i] = list[i];
		}

		// Stores the right half of the list
		for (int i = 0, j = leftSize; j < list.length; i++, j++) {
			right[i] = list[j];
		}

		// Recursively splits the sublists
		left = mergeSort(left);
		right = mergeSort(right);

		// 
		return merge(left, right);
	}

	/**
	 * Sorts and merges the elements of two lists to create a single sorted list.
	 *
	 * @param left List with the left half of a sequence
	 * @param right List with the right half of a sequence
	 * @return A sorted list resulting from merging the two given lists
	 */
	private static int[] merge(int[] left, int[] right) {

		// Lengths of both lists
		int leftLength = left.length;
		int rightLength = right.length;
		int[] result = new int[leftLength + rightLength];

		// Sets of indexes
		int idx = 0;
		int leftIdx = 0;
		int rightIdx = 0;

		// Goes through both lists (as long as there are any elements in either of them)
		while (leftLength > 0 || rightLength > 0) {

			// Checks if both lists have elements
			if (leftLength > 0 && rightLength > 0) {
				if (left[leftIdx] <= right[rightIdx]) {
					result[idx++] = left[leftIdx++];
					--leftLength;
				}
				else {
					result[idx++] = right[rightIdx++];
					--rightLength;
				}
			}
			// Add the current element of the left list
			else if (leftLength > 0) {
				result[idx++] = left[leftIdx++];
				--leftLength;
			}
			// Add the current element of the right list
			else if (rightLength > 0) {
				result[idx++] = right[rightIdx++];
				--rightLength;
			}
		}

		return result;
	}
}
