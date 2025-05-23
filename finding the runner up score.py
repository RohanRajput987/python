'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints : 2<=n<=10,-100<=A[i]<=100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.'''


if __name__ == '__main__':
    n = int(input())
    if(n>2 and n<=10):
        arr = list(map(int, input().split()))
    first=second=float("-inf")
    for i in arr:
        if i>first:
            second=first
            first=i
        elif i>second and i!=first:
            second=i
print(second)    
       