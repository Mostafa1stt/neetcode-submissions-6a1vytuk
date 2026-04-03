class Solution {
public:

    vector<int>index;
    int sizel;
    string encode(vector<string>& strs) {
        sizel = strs.size();
        int total=0;
        string res;
        for(int i=0; i<strs.size(); i++)
        {
            total += strs[i].size();
            index.push_back(total);
            res += strs[i];
        }

        return  res;
    }

    vector<string> decode(string s) {
        if(index.empty())
        {
            return {};
        }
        int counter;
        int i=0;
        int curent=0;
        int to = index[curent] ;
        vector<string> res ;
        string lol;
        do{
            counter++;
            lol.clear();
            if(to == i)
            {
                res.push_back("");
            }
            else
            {
                for(i;i<to; i++)
                {
                    lol += s[i];    
                }
                res.push_back(lol);
            }
            curent++;
            to = index[curent];
        }while(counter<sizel);
        return res;

    }
};
