#include <cmath>
#include <map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int counter[1001]= {0};
        int neg_counter[1001]= {0};
        int maxi = 0;
        vector<int>output;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]<0)
            {
                neg_counter[abs(nums[i])]++;
                if(neg_counter[abs(nums[i])]>maxi)
                {
                    maxi=neg_counter[abs(nums[i])];
                }

            }else
            {
                counter[nums[i]]++;
                if(counter[nums[i]]>maxi)
                {
                    maxi=counter[nums[i]];
                }
            }
        }
        do{
            for(int i =0; i<1001;i++)
            {
                if(counter[i]==maxi){
                    if(k == 0)
                    {
                        break;
                    }
                    output.push_back(i);
                    k--;
                }
            }
            for(int i =1; i<1001;i++)
            {
                if(neg_counter[i]==maxi){
                    if(k == 0)
                    {
                        break;
                    }
                    output.push_back(-i);
                    k--;
                }
            }
            maxi--;
        }while(k>0);
        return output;
    }
};
