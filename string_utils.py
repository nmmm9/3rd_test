def count_vowels(text):
    """주어진 문자열에서 모음의 개수를 반환합니다."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def reverse_text(text):
    """문자열을 거꾸로 뒤집습니다."""
    # 슬라이싱을 사용하여 문자열을 거꾸로 뒤집습니다.
    return text[::-1]

if __name__ == "__main__":
    sample = "Hello GitHub!"
    print("원본:", sample)
    print("모음 개수:", count_vowels(sample))
    print("뒤집은 텍스트:", reverse_text(sample))
```

위 코드에서 `reverse_text` 함수의 슬라이싱 오류를 수정했습니다. 원래 `text[::1]`로 되어 있어 문자열이 그대로 반환되었으나, `text[::-1]`로 수정하여 문자열을 올바르게 거꾸로 뒤집도록 했습니다.