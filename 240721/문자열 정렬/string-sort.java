import java.util.*;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner Sc = new Scanner(System.in);
        String str = Sc.next();
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        String sortedStr = new String(chars);
        System.out.println(sortedStr);
        
    }
}