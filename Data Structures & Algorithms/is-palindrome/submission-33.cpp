class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !isAlnum(s[l])) {
                l++;
            }
            while (l < r && !isAlnum(s[r])) {
                r--;
            }
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    bool isAlnum(char c) {
        return ('a' <= c && c <= 'z') || 
               ('A' <= c && c <= 'Z') || 
               ('0' <= c && c <= '9');
    }
};
