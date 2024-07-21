import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        int N = Sc.nextInt();
        int k = Sc.nextInt();
        int[] arr = new int[N];
        for(int i = 0; i<N; i++){
            arr[i] = Sc.nextInt();
        }

        Arrays.sort(arr);

        System.out.println(arr[k-1]);


    
    }


}