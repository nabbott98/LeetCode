/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  n > 0 && nums1.splice(-n)

  nums2.forEach((num) => {
    let maybeIndex

    if (nums1[0] > num) { maybeIndex = 0 } 
    else if (nums1[nums1.length - 1] < num) { maybeIndex = nums1.length } 
    else { maybeIndex = nums1.findIndex((n) => n > num) }

    nums1.splice(maybeIndex, 0, num)
  })
};