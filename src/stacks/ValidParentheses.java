/**
 * @lc id=20
 * @lc title=Valid Parentheses
 * @lc difficulty=Easy
 * @lc time=O(n)
 * @lc space=O(n)
 */
package stacks;

import java.util.Stack;

public class ValidParentheses {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ('[')) {
                stack.push(c);
            } else if (c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();

                if (c == ')' && top != '(') return false;
                if (c == ']' && top != '[') return false;
                if (c == '}' && top != '{') return false;
            }
        }
        return stack.isEmpty();
    }

   public static void main(String[] args) {
        ValidParentheses vp = new ValidParentheses();
        String s = "{(())}";
        boolean isvp = vp.isValid(s);
        System.out.println(isvp);
    }
}
