# LeetCode Solutions
These are solutions for leetcode problems written in Python. Problems are from [LeetCode China](https://leetcode-cn.com/problems/two-sum).

## 1.Two Sum
<br>Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
<br>Solution Code: [1_two_sum.py](./1_two_sum.py)

## 2.Add Two Numbers
<br>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
<br>Solution Code: [2_add_two_numbers.py](./2_add_two_numbers.py)

## 3.Longest Substring Without Repeating Characters
<br>Given a string, find the length of the longest substring without repeating characters.
<br>Solution Code: [3_longest_substring_without_repeat_chars.py](./3_longest_substring_without_repeat_chars.py)

## 4.Median of Two Sorted Arrays
<br>There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
<br>Solution Code: [4_median_of_two_sorted_arrays.py](./4_median_of_two_sorted_arrays.py)

## 5.Longest Palindromic Substring
<br>Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. (A palindromic string is a string which equals to its reverse).
<br>Solution Code: [5_longest_palindromic_substring.py](./5_longest_palindromic_substring.py). I use dynamic programming, but the solution seems a bit slow, only beats about 30% users.

## 6.ZigZag Conversion
<br>The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
<br>    &emsp;&emsp;&emsp;P&emsp;&ensp;&emsp;A&emsp;&ensp;&emsp;H&emsp;&ensp;&emsp;N
<br>    &emsp;&emsp;&emsp;A&emsp;P&emsp;L&emsp;S&emsp;I&emsp;I&emsp;G
<br>    &emsp;&emsp;&emsp;Y&emsp;&ensp;&emsp;I&emsp;&ensp;&emsp;R
<br>And then read line by line: "PAHNAPLSIIGYIR"
<br>Write the code that will take a string and make this conversion given a number of rows
<br>Solution Code: [6_zigzag_conversion.py](./6_zigzag_conversion.py). 

## 7.Reverse Integer
<br>Given a 32-bit signed integer, reverse digits of an integer.
<br>Solution Code: [7_reverse_integer.py](./7_reverse_integer.py). 

## 8.String to Integer (atoi)
<br>Implement atoi which converts a string to an integer.
<br>The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
<br>The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
<br>If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
<br>If no valid conversion could be performed, a zero value is returned.
<br>**Note:**
* Only the space character ' ' is considered as whitespace character.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is  returned.

<br>Solution Code: [8_string_to_integer.py](./8_string_to_integer.py). 

## 9.Palindrome Number
<br>Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
<br>Solution Code: [9_palindrome_number.py](./9_palindrome_number.py). 

## 10.Regular Expression Matching
<br>Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
<br>&emsp;&emsp;'.' Matches any single character.
<br>&emsp;&emsp;'*' Matches zero or more of the preceding element.
<br>The matching should cover the entire input string (not partial).
<br>**Note:**
* s could be empty and contains only lowercase letters a-z.
* p could be empty and contains only lowercase letters a-z, and characters like . or *.

<br>Solution Code: [10_regular_expression_matching.py](./10_regular_expression_matching.py). 

## 11.Container with Most Water
<br>Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
<br>**Note:** You may not slant the container and n is at least 2.
![question_11](./fig/question_11.jpg)
<br>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
<br>Solution Code: [11_container_with_most_water.py](./11_container_with_most_water.py). 

## 12.Integer to Roman
<br>Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
| Symbol | Value |
| :----  | :---- |
|I|1|
|V |5  |
|X |10 |
|L |50 |
|C |100 |
|D |500 |
|M |1000 |

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
<br>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9. 
* X can be placed before L (50) and C (100) to make 40 and 90. 
* C can be placed before D (500) and M (1000) to make 400 and 900.

<br>Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
<br>Solution Code: [12_integer_to_roman.py](./12_integer_to_roman). 

## 13.Roman to Integer
<br>Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
| Symbol | Value |
| :----  | :---- |
|I|1|
|V |5  |
|X |10 |
|L |50 |
|C |100 |
|D |500 |
|M |1000 |

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
<br>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

* I can be placed before V (5) and X (10) to make 4 and 9. 
* X can be placed before L (50) and C (100) to make 40 and 90. 
* C can be placed before D (500) and M (1000) to make 400 and 900.

<br>Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
<br>Solution Code: [13_roman_to_integer.py](./13_roman_to_integer.py). 


## 14.Longest Common Prefix
<br>Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".
<br>Solution Code: [14_longest_common_prefix.py](./14_longest_common_prefix.py). 

## 15.3Sum
<br>Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
<br>**Note:** The solution set must not contain duplicate triplets.
<br>Solution Code: [15_3sum.py](./15_3sum.py). 

## 16.3Sum Closest
<br>Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
<br>Solution Code: [16_3sum_closest.py](./16_3sum_closest.py). 

## 17.Letter Combinations of a Phone Number
<br>Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
<br>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
![question_17](./fig/question_17.png)
<br>Solution Code: [17_letter_combinations_of_a_phone_number.py](./17_letter_combinations_of_a_phone_number.py). 


## 18.4Sum
<br>Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
<br>**Note:** The solution set must not contain duplicate triplets.
<br>Solution Code: [18_4sum.py](./18_4sum.py). 

## 19.Remove Nth Node From End of List
<br>Given a linked list, remove the n-th node from the end of list and return its head.
<br>**Example:**
<br>Given linked list: 1->2->3->4->5, and n = 2.
<br>After removing the second node from the end, the linked list becomes 1->2->3->5.
<br>**Note:**
Given n will always be valid.
<br>**Follow up:**
<br>Could you do this in one pass?
<br>Solution Code: [19._remove_nth_node_from_end_of_list.py](./19._remove_nth_node_from_end_of_list.py). 

## 20.Valid Parentheses
<br>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
<br>An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

<br>Note that an empty string is also considered valid.
<br>Solution Code: [20_valid_parentheses.py](./20_valid_parentheses.py). 


## 21.Merge Two Sorted Lists
<br>Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
<br>Solution Code: [21_merge_two_sorted_lists.py](./21_merge_two_sorted_lists.py). 


## 22.Generate Parentheses
<br>Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
<br>For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
<br>Solution Code: [22_generate_parentheses.py](./22_generate_parentheses.py). 

## 23.Merge k Sorted Lists
<br>Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
<br>Solution Code: [23_merge_k_sorted_lists.py](./23_merge_k_sorted_lists.py). 


## 24.Swap Nodes in Pairs
<br>Given a linked list, swap every two adjacent nodes and return its head.
You may **not** modify the values in the list's nodes, only nodes itself may be changed.
<br>Solution Code: [24_swap_nodes_in_pairs.py](./24_swap_nodes_in_pairs.py). 

## 25.Reverse Nodes in k-Group
<br>Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
<br>**Example:**
<br>Given this linked list: 1->2->3->4->5
<br>For k = 2, you should return: 2->1->4->3->5
<br>For k = 3, you should return: 3->2->1->4->5
<br>**Note:**

* Only constant extra memory is allowed.
* You may not alter the values in the list's nodes, only nodes itself may be changed.

<br>Solution Code: [25_reverse_nodes_in_k-group.py](./25_reverse_nodes_in_k-group.py). 

## 26.Remove Duplicates from Sorted Array
<br>Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
<br>Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
<br>Solution Code: [26_remove_duplicates_from_sorted_array.py](./26_remove_duplicates_from_sorted_array.py). 

## 27.Remove Element
<br>Given an array nums and a value val, remove all instances of that value in-place and return the new length.
<br>Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
<br>The order of elements can be changed. It doesn't matter what you leave beyond the new length.
<br>Solution Code: [27_remove_element.py](./27_remove_element.py). 

## 28.Implement strStr()
<br>Implement strStr().Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
<br>**Clarification:**
<br>What should we return when needle is an empty string? This is a great question to ask during an interview.
<br>For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
<br>Solution Code: [28_implement_strStr().py](./28_implement_strStr().py). 

## 29.Divide Two Integers
<br>Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator. Return the quotient after dividing dividend by divisor. The integer division should truncate toward zero.
<br>**Note:**

* Both dividend and divisor will be 32-bit signed integers.
* The divisor will never be 0.
* Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2<sup>31</sup>,  2<sup>31</sup> − 1]. For the purpose of this problem, assume that your function returns 2<sup>31</sup> − 1 when the division result overflows.

<br>Solution Code: [29_divide_two_integers.py](./29_divide_two_integers.py). 

## 30.Substring with Concatenation of All Words
<br>You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
<br>Solution Code: [30_substring_with_concatenation_of_all_words.py](./30_substring_with_concatenation_of_all_words.py). 

## 31.Next Permutation
<br>Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
<br>This problem requires you to find the smallest number that larger than the given number by rearranging the order of numbers on each digit.
<br>Solution Code: [31_next_permutation.py](./31_next_permutation.py). 


## 32.Longest Valid Parentheses
<br>Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
<br>Solution Code: [32_longest_valid_parentheses.py](./32_longest_valid_parentheses.py). 

## 33.Search in Rotated Sorted Array
<br>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume no duplicate exists in the array. Your algorithm's runtime complexity must be in the order of O(log n).
<br>Solution Code: [33_search_in_rotated_sorted_array.py](./33_search_in_rotated_sorted_array.py).

## 34.Find First and Last Position of Element in Sorted Array
<br>Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1].
<br>Solution Code: [34_find_first_and_last_position_of_element_in_sorted_array.py](./34_find_first_and_last_position_of_element_in_sorted_array.py).

## 35.Search Insert Position
<br>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.
<br>Solution Code: [35_search_insert_position.py](./35_search_insert_position.py).

## 36.Valid Sudoku
<br>Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

<br>The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
<br>**Note:**

* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.
* The given board contain only digits 1-9 and the character '.'.
* The given board size is always 9x9.

<br>Solution Code: [36_valid_sudoku.py](./36_valid_sudoku.py).

## 37.Sudoku Solver
<br>Write a program to solve a Sudoku puzzle by filling the empty cells.
<br>A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

<br>Empty cells are indicated by the character '.'.
<br>**Note:**

* The given board contain only digits 1-9 and the character '.'.
* You may assume that the given Sudoku puzzle will have a single unique solution.
* The given board size is always 9x9.

<br>Solution Code: [37_sudoku_solver.py](./37_sudoku_solver.py).



## 38.Count and Say
<br>The count-and-say sequence is the sequence of integers with the first five terms as following:
1. 1
2. 11
3. 21
4. 1211
5. 111221

<br>1 is read off as "one 1" or 11.
<br>11 is read off as "two 1s" or 21.
<br>21 is read off as "one 2, then one 1" or 1211.
<br>Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.
<br>**Note:** Each term of the sequence of integers will be represented as a string.
<br>Solution Code: [38_count_and_say.py](./38_count_and_say.py).

## 39.Combination Sum
<br>Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
<br>The same repeated number may be chosen from candidates unlimited number of times.
<br>**Note:**

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

<br>Solution Code: [39_combination_sum.py](./39_combination_sum.py).

## 40.Combination Sum II
<br>Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target. Each number in candidates may only be used once in the combination.
<br>**Note:**

* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.

<br>Solution Code: [40_combination_sum_2.py](./40_combination_sum_2.py).

## 41.First Missing Positive
<br>Given an unsorted integer array, find the smallest missing positive integer.
<br>Solution Code: [41_first_missing_positive.py](./41_first_missing_positive.py).

## 42.Trapping Rain Water
<br>Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![question_42](./fig/question_42.png)
<br>The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
<br>Solution Code: [42_trapping_rain_water.py](./42_trapping_rain_water.py).

## 43.Multiply Strings
<br>Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
<br>Solution Code: [43_multiply_string.py](./43_multiply_string.py).

## 44.Wildcard Matching
<br>Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
<br> '?' Matches any single character.
<br> '*' Matches any sequence of characters (including the empty sequence).
<br>The matching should cover the entire input string (not partial).
<br>**Note:**

* s could be empty and contains only lowercase letters a-z.
* p could be empty and contains only lowercase letters a-z, and characters like ? or *.

<br>Solution Code: [44_wildcard_matching.py](./44_wildcard_matching.py).

## 45.Jump Game II
<br>Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.
<br>**Note:** You can assume that you can always reach the last index.
<br>Solution Code: [45_jump_game_2.py](./45_jump_game_2.py).

## 46.Permutations
<br>Given a collection of distinct integers, return all possible permutations.
<br>Solution Code: [46_permutations.py](./46_permutations.py).

## 47.Permutations II
<br>Given a collection of numbers that might contain duplicates, return all possible unique permutations.
<br>Solution Code: [47_permutations_2.py](./47_permutations_2.py).

## 48.Rotate Image
<br>You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).
<br>**Note:**
<br>You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
<br>Solution Code: [48_rotate_image.py](./48_rotate_image.py).

## 49.Group Anagrams
<br>Given an array of strings, group anagrams together.
<br>Solution Code: [49_group_anagrams.py](./49_group_anagrams.py).

## 50.Power(x,n)
<br>Implement pow(x, n), which calculates x raised to the power n (x<sup>n</sup>).
<br>Solution Code: [50_power_x_n.py](./50_power_x_n.py).

## 51.N-Queens
<br>The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. 
Given an integer n, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
<br>Solution Code: [51_n_queens.py](./51_n_queens.py).

## 52.N-Queens
<br>The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. 
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
<br>Solution Code: [52_n_queens_2.py](./52_n_queens_2.py).


## 53.Maximum Subarray
<br>Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
<br>Solution Code: [53_maximum_subarray.py](./53_maximum_subarray.py).

## 54.Spiral Matrix
<br>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
<br>Solution Code: [54_spiral_matrix.py](./54_spiral_matrix.py).

## 55.Jump Game
<br>Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
<br>Solution Code: [55_jump_game.py](./55_jump_game.py).

## 56.Merge Intervals
<br>Given a collection of intervals, merge all overlapping intervals.
<br>Solution Code: [56_merged_intervals.py](./56_merged_intervals.py).

## 57.Insert Interval
<br>Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
<br>Solution Code: [57_insert_interval.py](./57_insert_interval.py).

## 58.Length of Last Word
<br>Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
<br>Note: A word is defined as a maximal substring consisting of non-space characters only.
<br>Solution Code: [58_length_of_last_word.py](./58_length_of_last_word.py).

## 59.Spiral Matrix II
<br>Given a positive integer n, generate a square matrix filled with elements from 1 to n<sup>2</sup> in spiral order.
<br>Solution Code: [59_spiral_matrix_2.py](./59_spiral_matrix_2.py).

## 60.Permutation Sequence
<br>The set [1,2,3,...,n] contains a total of n! unique permutations.
<br>By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

1.  "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

<br>Given n and k, return the kth permutation sequence.
<br>**Note:**
<br>Given n will be between 1 and 9 inclusive.
<br>Given k will be between 1 and n! inclusive.
<br>Solution Code: [60_permutation_sequence.py](./60_permutation_sequence.py).

## 61.Rotate List
<br>Given a linked list, rotate the list to the right by k places, where k is non-negative.
<br>Solution Code: [61_rotate_list.py](./61_rotate_list.py).