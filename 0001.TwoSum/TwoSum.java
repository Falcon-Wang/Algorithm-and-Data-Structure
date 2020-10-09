package algorithm.leetcode.easy;

/**
 * @program: Algorithm
 * @description: LeetCode第一题-两数之和
 * @author: FalconWang王皓伟
 * @create: 2020-09-25-11-15
 */
public class TwoSum
{
    public static void main(String[] args){
        //测试
        int[] testArr = {3,2,4};
        int target = 6;

        Solution solution = new Solution();
        int[] sol = solution.twoSum(testArr,target);

        System.out.println("["+sol[0]+","+sol[1]+"]");
    }
}
/*
需求：
给出一个整型一维数组nums[],一个target
要求搜索数组，找出两数相加等于target的唯一解
example：
int[] nums = [1,3,2,4];
int target = 3;
OUTPUT -----> nums[0] + nums[2] = target(3)
 */
class Solution
{
    /**
     *
     * @param nums 原始数组
     * @param target 目标数据
     * @return 包含目标数据组成元素的数组
     */
    public int[] twoSum(int[] nums,int target)
    {
        int[] arr = new int[2];
        for (int x=0;x<nums.length;x++)
        {
            for (int y=x+1;y<nums.length;y++)
            {
                if (nums[x] + nums[y] == target)
                {
                    arr[0] = x;
                    arr[1] = y;
                }
            }
        }
        return arr;
    }
}
