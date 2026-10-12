public class Solution {
    public bool IsPalindrome(string s) {
        if(string.IsNullOrEmpty(s)) return true;
        s = ValidString(s);
        Console.WriteLine(s);
        int l=0,r=s.Length-1;
        while(l<r){
            if(s[l]!=s[r])
                return false;
            l++;
            r--;
        }
        return true;
    }
    public string ValidString(string s){
        List<char> result = new List<char>();
        foreach(var ch in s)
        {
            if(Char.IsLetterOrDigit(ch)){
                result.Add(Char.ToLower(ch));
            }
        }
        return string.Join("",result);
    }
}
