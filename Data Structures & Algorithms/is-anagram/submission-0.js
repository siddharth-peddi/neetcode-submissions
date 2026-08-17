class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) {
            return false;
        }
        let map = new Map ();
        for (let i = 0; i < s.length; i++) {
            const char = s[i];
            map.set (char, (map.get(char) || 0) + 1);
        }     
        for (let i = 0; i < t.length; i++) {
            const char = t[i];
            map.set (char, (map.get(char) || 0) - 1);
        }
        for (const count of map.values()) {
            if(count !== 0) {
                return false;
            }
        }
    return true;    
    }
}