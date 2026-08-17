class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const count = new Map();

    for (const num of nums) {
        count.set(num, (count.get(num) || 0) + 1);
    }

    const entries = Array.from(count.entries());

    entries.sort((a, b) => b[1] - a[1]);

    const topK = entries.slice(0, k);

    const result = topK.map(entry => entry[0]);

    return result;
    }
}
