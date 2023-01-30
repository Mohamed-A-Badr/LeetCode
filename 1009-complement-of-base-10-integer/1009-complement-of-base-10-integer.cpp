class Solution {
public:
    int bitwiseComplement(int n) {
        if(n == 0)
            return 1;
        string s = "";
        while(n){
            int x = (n & 1);
            s += '0' + (!x);
            n >>= 1;
        }
        reverse(s.begin(), s.end());
        long long res = stoi(s, 0, 2);
        return res;
    }
};