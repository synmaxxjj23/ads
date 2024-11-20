import java.util.Scanner;

public class quick {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = { 7, -1, 2, 3, 11, -8, 6, 9 };
        QS(arr, 0, 7);
    }

    public static void QS(int[] arr, int low, int high) {
        if (low < high) {
            int j = parts(arr, low, high);
            QS(arr, low, j - 1);
            QS(arr, j + 1, high);
        }
    }

    public static int parts(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        print(arr);
        return i + 1;
    }

    public static void print(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}