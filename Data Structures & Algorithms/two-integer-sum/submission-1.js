class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * nums = [2, 7, 11, 15]
    target = 9
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