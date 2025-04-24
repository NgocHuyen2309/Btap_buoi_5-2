
"""
 ▸Tạo 1 danh sách (list) ngẫu nhiên N phần tử (N nhập từ bàn phím) có giá trị từ 1 đến 100 sau đó tạo 1 menu cho phép thực hiện các công việc sau:
In ra danh sách vừa tạo.
In đảo ngược danh sách.
Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
In ra vị trí các phần tử là số nguyên tố.
tìm các số duy nhất (không trùng lặp) trong danh sách.
liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
In ra các đoạn con trong danh sách giảm liên tiếp.
"""
import random
import os

def menu():
    print("---------------------------------------------MENU---------------------------------------")
    print("\t 1. In ra danh sách vừa tạo.")
    print("\t 2. In đảo ngược danh sách.")
    print("\t 3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).")
    print("\t 4. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.")
    print("\t 5. Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.")
    print("\t 6. In ra vị trí các phần tử là số nguyên tố.")
    print("\t 7. Tìm các số duy nhất (không trùng lặp) trong danh sách.")
    print("\t 8. Liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.")
    print("\t 9. In ra các đoạn con trong danh sách giảm liên tiếp.")
    print("\t10. Thoát.")
    cl = int(input("Chọn lựa của bạn (1-10): "))
    return cl

def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cac_doan_giam(ds):
    result = []
    temp = [ds[0]]
    for i in range(1, len(ds)):
        if ds[i] < ds[i - 1]:
            temp.append(ds[i])
        else:
            if len(temp) > 1:
                result.append(temp[:])
            temp = [ds[i]]
    if len(temp) > 1:
        result.append(temp)
    return result

def main():
    n = int(input("Nhập số phần tử của danh sách: "))
    ds = [random.randint(1, 100) for _ in range(n)]

    while True:
        cl = menu()
        if cl == 1:
            print("Danh sách:", ds)
        elif cl == 2:
            print("Danh sách đảo ngược:", ds[::-1] )
        elif cl == 3:
            print("Danh sách sau khi sắp xếp:", sorted(ds))
        elif cl == 4:
            max_val = max(ds)
            pos = len(ds) - 1 - ds[::-1].index(max_val)
            print(f"Giá trị lớn nhất là {max_val}, vị trí cuối cùng: {pos}")
        elif cl == 5:
            x = int(input("Nhập giá trị X cần tìm: "))
            count = ds.count(x)
            positions = [i for i, val in enumerate(ds) if val == x]
            print(f"Số lần xuất hiện của {x}: {count}")
            print("Vị trí xuất hiện:", positions)
        elif cl == 6:
            primes_pos = [i for i, val in enumerate(ds) if la_nguyen_to(val)]
            print("Vị trí các số nguyên tố:", primes_pos)
        elif cl == 7:
            unique = [val for val in ds if ds.count(val) == 1]
            print("Các số duy nhất:", unique)
        elif cl == 8:
            counted = {}
            for val in ds:
                counted[val] = counted.get(val, 0) + 1
            for val, count in counted.items():
                print(f"Giá trị {val} xuất hiện {count} lần")
        elif cl == 9:
            subseqs = cac_doan_giam(ds)
            print("Các đoạn con giảm liên tiếp:")
            for sub in subseqs:
                print(sub)
        elif cl == 10:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == '__main__':
    os.system('')
    main()




