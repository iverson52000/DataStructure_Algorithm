const nums = [0, -1, 3, 4, -5, 0];

const maxSubArray = (nums) => {
  const res = { result: nums[0], indexes: [0, 0] };
  let curSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > curSum + nums[i]) {
      curSum = nums[i];
      res.indexes[0] = i;
    } else {
      curSum += nums[i];
    }

    if (curSum > res.result) {
      res.result = curSum;
      res.indexes[1] = i;
    }
  }
  return res;
};

console.log(maxSubArray(nums));
