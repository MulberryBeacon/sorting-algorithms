import { SortAlgorithm } from '@mulberrybeacon/sorting/lib/SortAlgorithm';

/**
 * Several possible implementations of the Merge Sort algorithm.
 * 
 * @author Eduardo Ferreira
 */
export class MergeSort {

    /**
     * Top-down version of Merge Sort.
     *
     * @param {int[]} list List of numbers
     * @return {int[]} A sorted list resulting from merging the two given lists
     */
    mergeSort(list) {

        // Checks if the list is already sorted
        if (list.length <= 1) {
            return list;
        }

        // Lists to store the left and right sides of the list
        const leftSize = list.length / 2;
        let left = new int[leftSize];
        let right = new int[list.length - leftSize];

        // Stores the left half of the list
        for (let i = 0; i < leftSize; i++) {
            left[i] = list[i];
        }

        // Stores the right half of the list
        for (let i = 0, j = leftSize; j < list.length; i++, j++) {
            right[i] = list[j];
        }

        // Recursively splits the sublists
        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

    /**
     * Sorts and merges the elements of two lists to create a single sorted list.
     *
     * @param {int[]} left List with the left half of a sequence
     * @param {int[]} right List with the right half of a sequence
     * @return {int[]} A sorted list resulting from merging the two given lists
     */
    merge(left, right) {

        // Lengths of both lists
        let leftLength = left.length;
        let rightLength = right.length;
        let result = new int[leftLength + rightLength];

        // Sets of indexes
        let idx = 0;
        let leftIdx = 0;
        let rightIdx = 0;

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
