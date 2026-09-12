class Solution {
public:
    bool isValid(string s) {
        stack<char> stk; 
        unordered_map<char, char> hmap;
        hmap['{'] = '}';
        hmap['('] =')';
        hmap['['] = ']';
        for (char c : s) {
            if (hmap.contains(c)) {
                stk.push(c);
            }
            else {
                if (stk.empty() || c != hmap[stk.top()]) {
                    return false;
                }
                stk.pop();
            }
        }
        return stk.empty();
    }
};
