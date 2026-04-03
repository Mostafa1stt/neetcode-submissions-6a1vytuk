class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string>lol = strs;
        vector<vector<string>>output ={};
        vector<string>totalstrings={};
        bool checker ;
        for(int i=0;i<strs.size();i++)
        {
            checker = false;
            for(auto a:totalstrings)
            {
                if( a == lol[i])
                {
                    checker = true;
                }
            }
            if(checker==true)
            {
                continue ; 
            }
            vector<string>strings={};
            for(int j=i+1;j<strs.size();j++)
            {
                if(strs[i].size()!=strs[j].size())
                {
                    continue;
                }
                sort(strs[i].begin(),strs[i].end());
                sort(strs[j].begin(),strs[j].end());
                if(strs[i] == strs[j])
                {
                    strings.push_back({lol[j]});
                    totalstrings.push_back({lol[j]});
                }
            }
            
            strings.push_back({lol[i]});   
            output.push_back({strings});
        }
        return output;
    }
};
