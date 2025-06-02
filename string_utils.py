```python
def count_vowels(text):
    """주어진 문자열에서 모음의 개수를 반환합니다."""
    vowels = 'aeiouAEIOU'
    # 모음을 찾기 위해 문자열을 순회하면서 모음에 해당하는 문자가 있는지 확인합니다.
    return sum(1 for char in text if char in vowels)

def reverse_text(text):
    """문자열을 거꾸로 뒤집습니다."""
    # 문자열을 거꾸로 뒤집기 위해 슬라이싱을 사용합니다.
    return text[::-1]

if __name__ == "__main__":
    sample = "Hello GitHub!"
    print("원본:", sample)
    print("모음 개수:", count_vowels(sample))
    print("뒤집은 텍스트:", reverse_text(sample))
```

### 설명
- `reverse_text` 함수에서 문자열을 거꾸로 뒤집기 위해 슬라이싱을 잘못 사용하고 있었습니다. `text[::1]`는 원본 문자열을 그대로 반환하므로, `text[::-1]`로 수정하여 문자열을 올바르게 뒤집도록 했습니다.
- `count_vowels` 함수는 이미 올바르게 작동하고 있으므로 수정할 필요가 없었습니다.