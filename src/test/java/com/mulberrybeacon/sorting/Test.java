public class Test {
	public static void main(String[] args) {
		/*int[] list = {4,8,3,10,487,42,6762,91,2,168,34,1};
		BubbleSort.bubbleSort(list, 2);
		for (int i = 0; i < list.length; i++) {
			System.out.println(list[i]);
		}*/

		int[] list = {4,8,5,6,1};
		BubbleSort.bubbleSort(list, 0);
		for (int i = 0; i < list.length; i++) {
			System.out.println(list[i]);
		}

		System.out.println("===============================");

		int[] listMerge = {38, 27, 43, 3, 9, 82, 10};
		listMerge = MergeSort.mergeSort(listMerge);
		for (int i = 0; i < listMerge.length; i++) {
			System.out.println(listMerge[i]);
		}
	}
}
