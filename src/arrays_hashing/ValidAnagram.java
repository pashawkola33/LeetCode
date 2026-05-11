/**
 * @lc id=242
 * @lc title=Valid Anagram
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(1)
 */
package arrays_hashing;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
       int count[] = new int[26];
        if(s.length() != t.length()){
            return false;
        }
        for(int i = 0; i < s.length(); i++){
        count[s.charAt(i) - 'a']++;
        }
        for(int j = 0; j < t.length(); j++){
            count[t.charAt(j) - 'a']--;
        }
        for(int x = 0; x < count.length; x++){
            if(count[x] != 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        ValidAnagram anagram = new ValidAnagram();


        String as = "ass";
        String sa = "sas";
        boolean isanagram = anagram.isAnagram(as, sa);
        System.out.println(isanagram);
    }
}
