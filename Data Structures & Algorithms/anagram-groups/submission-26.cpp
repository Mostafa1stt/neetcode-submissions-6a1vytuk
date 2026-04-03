class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mymap;
        vector<vector<string>> result;

        for (string s: strs) {
            string sorted_string = s;
            sort(sorted_string.begin(), sorted_string.end());
            mymap[sorted_string].push_back(s);
        }
        for (auto it: mymap)
            result.push_back(it.second);

        return result;
    }
};
