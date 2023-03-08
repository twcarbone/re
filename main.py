import re


def main():
    with open("./sample/numbers.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        nums = []
        for first, second in re.findall(pattern="(\d+)\s*-\s*(\d+)", string=line):
            nums.extend(list(range(int(first), int(second) + 1)))

        for num in re.findall(pattern=r"[^-]\s*(\d+)\s*[^-]", string=line):  # Needs more work
            nums.append(int(num))
        
        print(line + " : " + ", ".join([f"{num:0>3}" for num in sorted(nums)]))

if __name__ == "__main__":
    main()