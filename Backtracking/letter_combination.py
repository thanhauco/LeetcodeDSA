from typing import List

def letter_combination(n: int) -> List[str]:
    res: List[str] = []

    def dfs(start_index: int, path: List[str]) -> None:
        if start_index == n:
            res.append("".join(path))
            return
        for letter in "ab":
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res

def test_letter_combination():
    assert letter_combination(1) == ["a", "b"], "Test case 1 failed"
    assert letter_combination(2) == ["aa", "ab", "ba", "bb"], "Test case 2 failed"
    assert letter_combination(0) == [""], "Test case 3 failed"
    print("All test cases passed!")

if __name__ == "__main__":
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)

    test_letter_combination()