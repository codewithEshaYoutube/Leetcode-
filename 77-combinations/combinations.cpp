class Solution {
public:


    void rawCombine(vector<vector<int>> &ret, vector<int> &current, int n, int k) {
        if (current.size() == k) {
            vector<int> r(current.begin(), current.end());
            ret.push_back(r);
        }

        int i = 1;
        if (current.size()) i = current.back()+1;

        for (; i <= n; ++i) {
            current.push_back(i);
            rawCombine(ret, current, n, k);
            current.pop_back();
        }
        
    }


    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> ret;
        vector<int> current;
        rawCombine(ret, current, n, k);
        return ret;
    }
};