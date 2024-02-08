def swap_pairs(text):
    # 对输入字符串中的每两个字符进行位置互换
    swapped_text = ""
    for i in range(0, len(text), 2):
        # 逐对提取字符并交换位置
        pair = text[i:i+2]
        swapped_pair = pair[1] + pair[0]  # 交换位置
        swapped_text += swapped_pair
    return swapped_text

def main():
    text = input("Enter the text to encode using UCS-2: ")
    if len(text) % 2 == 0:  # 检查字符串长度是否为偶数
        swapped_text = swap_pairs(text)
        print("UCS-2 encoded text:", swapped_text)
    else:
        print("Input string length must be even. Current character count:", len(text))

if __name__ == "__main__":
    main()
