```python
def count_vowels(text):
    """주어진 문자열에서 모음의 개수를 반환합니다."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def reverse_text(text):
    """문자열을 거꾸로 뒤집습니다."""
    return text[::-1]  # 문자열을 올바르게 뒤집기 위해 슬라이싱을 수정했습니다.

if __name__ == "__main__":
    sample = "Hello GitHub!"
    print("원본:", sample)
    print("모음 개수:", count_vowels(sample))
    print("뒤집은 텍스트:", reverse_text(sample))
```

### 주요 변경 사항
- `reverse_text` 함수에서 문자열을 올바르게 뒤집기 위해 슬라이싱을 `text[::1]`에서 `text[::-1]`로 수정했습니다. 

이 변경 사항은 문자열을 뒤집는 기능을 제대로 수행하도록 합니다. 다른 부분은 요청 사항이 없으므로 변경하지 않았습니다.