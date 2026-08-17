class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
    let store = new Map();

    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];

        if (store.has(complement)) {
            return [store.get(complement), i]
        }
    store.set(nums[i], i);
    }
}
}