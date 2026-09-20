class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        for (const char of s) {
            if (char === "(" || char === "[" || char === "{") {
                stack.push(char);
            } else if (char === "]") {
                if (stack[stack.length - 1] !== "[") {
                    return false;
                }
                stack.pop();
            } else if (char === ")") {
                if (stack[stack.length - 1] !== "(") {
                    return false;
                }
                stack.pop();
            } else if (char === "}") {
                if (stack[stack.length - 1] !== "{") {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.length === 0;
    }
}
