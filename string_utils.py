def count_vowels(text):
    """주어진 문자열에서 모음의 개수를 반환합니다."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def reverse_text(text):
    """문자열을 거꾸로 뒤집습니다."""
    # 오류 수정: [::1]을 [::-1]로 변경하여 문자열을 올바르게 뒤집습니다.
    return text[::-1]

if __name__ == "__main__":
    sample = "Hello GitHub!"
    print("원본:", sample)
    print("모음 개수:", count_vowels(sample))
    print("뒤집은 텍스트:", reverse_text(sample))
```

### 변경 사항 설명
- `reverse_text` 함수의 슬라이싱 부분에서 오류가 있었습니다. `text[::1]`은 문자열을 그대로 반환하므로, 문자열을 뒤집기 위해 `text[::-1]`로 수정하였습니다. 이로써 문자열이 올바르게 뒤집혀 반환됩니다.