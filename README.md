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



