class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> m = new HashMap<>();
        int c = 0;

        for(int i=0; i < nums.length; i++)
        {
            if(m.containsKey(nums[i]))
            {
                c = m.get(nums[i]) + 1;
                if(c > 1)
                {
                    return true;
                }
                m.put(nums[i],c);
            }
            else{
                m.put(nums[i],1);
            }
        }
        
        System.out.println(m);
        return false;
    }
}