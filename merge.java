import java.util.Scanner;

public class merge {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = { 7, -1, 2, 3, 11, -8, 6, 9 };
        MS(arr, 0, 7);
    }

    public static void MS(int[] arr, int low, int high) {
        if (low < high) {
            int mid = low + (high - low) / 2;
            MS(arr, 0, mid);
            MS(arr, mid + 1, high);
            Merge(arr, low, mid, high);
            print(arr);
        }

    }

    public static void print(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void Merge(int[] arr, int low, int mid, int high) {
        int[] brr = new int[high - low + 1];
        int i = low, j = mid + 1, k = 0;
        while (i <= mid && j <= high) {
            if (arr[i] > arr[j]) {
                brr[k++] = arr[j++];
            } else {
                brr[k++] = arr[i++];
            }
        }
        while (i <= mid) {
            brr[k++] = arr[i++];
        }
        while (j <= high) {
            brr[k++] = arr[j++];
        }
        for (int x = low; x <= high; x++) {
            arr[x] = brr[x - low];
        }

    }
}