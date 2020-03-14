# LeetCode Solutions
These are solutions for leetcode problems written in Python. Problems are from [LeetCode China](https://leetcode-cn.com/problems/two-sum).

## 去吃吃吃了嘿嘿

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


