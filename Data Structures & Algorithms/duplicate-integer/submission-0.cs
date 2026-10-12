public class Solution {
    public bool hasDuplicate(int[] nums) {
        //Approach 1 - Hashmap or HashSet

        HashSet<int> hash  = new HashSet<int>();
        foreach(var num in nums){
            if(hash.Contains(num))
                return true;
            hash.Add(num);
        }
        return false;
    }
}
