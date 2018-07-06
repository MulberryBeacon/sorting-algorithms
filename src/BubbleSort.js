import { SortAlgorithm } from '@mulberrybeacon/sorting/lib/SortAlgorithm';

/**
 * Several possible implementations of the Bubble Sort algorithm.
 * These will normally consist of a base version and a set of possible optimizations.
 * 
 * @author Eduardo Ferreira
 */
class BubbleSort {

    /**
     * Invokes the best available version of Bubble Sort.
     *
     * @param {int[]} list List of numbers
     */
    bubbleSort(list) {
        bubbleSort(list, 2);
    }

    /**
     * Defines the desired level of optimization when invoking Bubble Sort.
     *
     * @param {int[]} list List of numbers
     * @param {int} level Level of optimization
     */
    bubbleSort(list, level) {
        switch (level) {
            case 0:
                bubbleSortDumb(list);
                break;

            case 1:
                bubbleSortSmart(list);
                break;

            case 2:
                bubbleSortSmartest(list);
                break;

            default:
                break;
        }
    }

    /**
     * Straightforward (and dumb!) version of Bubble Sort.
     *
     * @param {int[]} list List of numbers
     */
    bubbleSortDumb(list) {
        for (let i = 0; i < list.length; i++) {
            for (let j = 0; j < list.length - 1; j++) {
                if (list[j] > list[j + 1]) {
                    SortAlgorithm.swapElements(list, j);
                }
            }
        }
    }

    /**
     * Smart version of Bubble Sort.
     * It assumes that the nth largest element is placed in its final position in the nth iteration.
     * The inner 'for' loop avoids looking at the last n-1 elements in its nth iteration.
     *
     * @param {int[]} list List of numbers
     */
    bubbleSortSmart(list) {
        for (let i = 1; i <= list.length; i++) {
            for (let j = 0; j < list.length - i; j++) {
                if (list[j] > list[j + 1]) {
                    SortAlgorithm.swapElements(list, j);
                }
            }
        }
    }

    /**
     * An even smarter version of Bubble Sort.
     * It memorizes the index of the last element to be switched and assumes that all the elements
     * onwards are in their final positions. The next iteration will proceed until the the memorized
     * index.
     *
     * @param {int[]} list List of numbers
     */
    bubbleSortSmartest(list) {
        const size = list.length;
        while (size > 0) {
            let idx = 0;
            for (let j = 0; j < size - 1; j++) {
                if (list[j] > list[j + 1]) {
                    SortAlgorithm.swapElements(list, j);
                    idx = j + 1;
                }
            }

            size = idx;
        }
    }
}
