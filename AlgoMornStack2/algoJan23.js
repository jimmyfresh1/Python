/* 
  Balance Index

  Here, a balance point is ON an index, not between indices.

  Return the balance index where sums are equal on either side
  (exclude its own value).

  Return -1 if none exist.

*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;


function balanceIndex(nums) {
    var totalSum = 0;
    for (var i = 0; i < nums.length; i++) {
        totalSum += nums[i];
    }

    var progressiveSum = 0;
    for (var i = 0; i < nums.length; i++) {
        if (progressiveSum === (totalSum - nums[i]) / 2) {
            return i;
        }
        progressiveSum += nums[i];
    }

    return -1;
}

console.log(balanceIndex(nums1)); // Should output 2
console.log(balanceIndex(nums2)); // Should output -1


// balanceIndex(nums1)
// console.log(balanceIndex(nums1));
// console.log(balanceIndex(nums2));
/***/