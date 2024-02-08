def swap_quads(text):
    # 对输入字符串中的每四个字符进行位置翻转
    swapped_text = ""
    for i in range(0, len(text), 4):
        # 逐四个提取字符并翻转位置
        quad = text[i:i+4]
        swapped_quad = quad[::-1]  # 翻转位置
        swapped_text += swapped_quad
    return swapped_text

def main():
    text = input("Enter the text to encode using UCS-4: ")
    if len(text) % 4 == 0:  # 检查字符串长度是否为4的倍数
        swapped_text = swap_quads(text)
        print("UCS-4 encoded text:", swapped_text)
    else:
        print("Input string length must be a multiple of 4. Current character count:", len(text))

if __name__ == "__main__":
    main()
