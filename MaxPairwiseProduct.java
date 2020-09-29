import java.util.*;
import java.io.*;

public class MaxPairwiseProduct {
    static long getMaxPairwiseProduct(int[] A) {
       // int index1 = 1, index2 =1;
       // for(int i = 2; i < A.length; i++){
         //   if(A[i] > A[index1])   index1 = i;
        //}
        //if( index1 == 1)  index2 = 2;
        //for(int i = 1; i < A.length; i++){
         //   if( i != index1 && A[i] > A[index2]) index2 = i;
        //}
int n = A.length;
Arrays.sort(A);
long result = (long) A[n-2]* A[n-1];        
return result;
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }
long result = getMaxPairwiseProduct(numbers);        
System.out.println(result);
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new
                    InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

}
