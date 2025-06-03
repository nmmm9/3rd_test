def count_vowels(text):
    """주어진 문자열에서 모음의 개수를 반환합니다."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def reverse_text(text):
    """문자열을 거꾸로 뒤집습니다."""
    # 오류 수정: 문자열을 거꾸로 뒤집기 위해 슬라이싱을 [::-1]로 수정
    return text[::-1]

if __name__ == "__main__":
    sample = "Hello GitHub!"
    print("원본:", sample)
    print("모음 개수:", count_vowels(sample))
    print("뒤집은 텍스트:", reverse_text(sample))
```

- `reverse_text` 함수에서 문자열을 거꾸로 뒤집는 슬라이싱이 잘못되어 있었습니다. `[::1]`은 문자열을 그대로 반환하므로, 이를 `[::-1]`로 수정하여 문자열을 올바르게 뒤집도록 했습니다.