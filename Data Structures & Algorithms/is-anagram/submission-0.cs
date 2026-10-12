public class Solution {
    public bool IsAnagram(string s, string t) {
        //Hashing
        if(string.IsNullOrEmpty(s)||string.IsNullOrEmpty(t))
            return false;
        if(s.Length!=t.Length)
            return false;
        Dictionary<char,int> map = new();//char-count
        foreach(var ch in s){
            if(!map.ContainsKey(ch)){
                map[ch]=1;
            }else{
                map[ch]++;
            }
        }

        //
        foreach(var ch in t){
            if(map.ContainsKey(ch) && map[ch]>0){
                map[ch]--;
            }else{
                return false;
            }
        }
        return true;
    }
}
