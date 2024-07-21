import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        int N = Sc.nextInt();
        String[] arr = new String[N];
        for (int i=0; i<N ; i++){
            arr[i] = Sc.next();
        }

        Arrays.sort(arr);

        for (int i=0; i<N ; i++){
            System.out.println(arr[i]);
        }
    
    
    }


}