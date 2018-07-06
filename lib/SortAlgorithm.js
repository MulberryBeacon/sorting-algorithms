/**
 * Set of generic and common functions for sort algorithms.
 *
 * @author Eduardo Ferreira
 */
export class SortAlgorithm {

    /**
     * Swaps a pair of elements.
     *
     * @param {int[]} list List of elements
     * @param {int} p1 First element of the pair
     * @param {int} p2 Second element of the pair
     */
    static swapElements(list, p1, p2) {
        const aux = list[p1];
        list[p1] = list[p2];
        list[p2] = aux;
    }
}
