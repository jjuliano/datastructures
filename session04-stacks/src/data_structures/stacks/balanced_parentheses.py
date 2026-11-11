from .stack import Stack


# Easy: brackets.easy, procedure Balanced(s, n). Stack is the pile,
# and bracket_pairs plays the part of Match(open, close).
def balanced_parentheses(parentheses: str) -> bool:
    """Use a stack to check if a string of parentheses is balanced.
    >>> balanced_parentheses("([]{})")
    True
    >>> balanced_parentheses("[()]{}{[()()]()}")
    True
    >>> balanced_parentheses("[(])")
    False
    >>> balanced_parentheses("1+2*3-4")
    True
    >>> balanced_parentheses("{}")
    True
    >>> balanced_parentheses("))((")
    False
    >>> balanced_parentheses("((")
    False
    >>> balanced_parentheses("")
    True
    """
    # Easy Balanced: array pile(1:n); top <- 0
    stack: Stack[str] = Stack()
    # Easy Match: ( pairs with ) and [ with ]. Python adds { and }.
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    # Easy Balanced: i <- 1; while i <= n do; ch <- s(i)
    for bracket in parentheses:
        # Easy Balanced: if ch = "(" or ch = "[" then
        if bracket in bracket_pairs:
            # Easy Balanced: top <- top + 1; pile(top) <- ch
            stack.push(bracket)
        # Easy Balanced: else [ if top = 0 then return(false)
        #   if Match(pile(top), ch) = false then return(false)
        #   top <- top - 1 ]. pop() reads the top and drops it.
        # Python skips characters that are not brackets.
        elif bracket in (")", "]", "}") and (
            stack.is_empty() or bracket_pairs[stack.pop()] != bracket
        ):
            return False
    # Easy Balanced: return(top = 0)
    return stack.is_empty()


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        not_str = "" if balanced_parentheses(example) else "not "
        print(f"{example} is {not_str}balanced")
