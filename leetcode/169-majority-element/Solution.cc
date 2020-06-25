class Solution {
public:
    // bit manipulation approach
    int majorityElement(vector<int>& nums) {
        int candidate=0;
        int n=nums.size();
        for(int i=0;i<32;++i)
        {
            int ones=0;

            for(int j=0;j<n;++j)
                if(nums[j] & 1<<i)
                    ones++;

            if(ones>(n-ones))
                candidate|=1<<i;
        }

        return candidate;

    }
};