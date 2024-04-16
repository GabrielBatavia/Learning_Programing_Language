
/**
 * persiapan_uts_smstr2
 */
public class persiapan_uts_smstr2 {

    //make a array object

    int a, b;

    public persiapan_uts_smstr2(int a, int b) {
        this.a = a;
        this.b = b;
    }

    public static void main(String[] args) {
    
        persiapan_uts_smstr2[] array = new persiapan_uts_smstr2[7];

        for (int i=0; i < array.length; i++) {
            array[i] = new persiapan_uts_smstr2(i, i * 2);
        }
    }
    

    
}
