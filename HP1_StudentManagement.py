# Khởi tạo danh sách học sinh rỗng
students = []

# Chương trình chính
while True:
    print("\nQuản lý danh sách học sinh:")
    print("1. Thêm học sinh")
    print("2. Sửa tên học sinh")
    print("3. Xóa học sinh")
    print("4. Xem danh sách học sinh")
    print("5. Thoát")

    choice = input("Chọn một tùy chọn (1-5): ")

    # Thêm học sinh
    if choice == "1":
        name = input("Nhập tên học sinh: ")
        students.append(name)
        print(f"Đã thêm học sinh: {name}")

    # Sửa tên học sinh
    elif choice == "2":
        name = input("Nhập tên học sinh cần sửa: ")
        if name in students:
            new_name = input("Nhập tên mới: ")
            index = students.index(name)
            students[index] = new_name
            print(f"Đã sửa tên học sinh {name} thành {new_name}")
        else:
            print("Không tìm thấy học sinh!")

    # Xóa học sinh
    elif choice == "3":
        name = input("Nhập tên học sinh cần xóa: ")
        if name in students:
            students.remove(name)
            print(f"Đã xóa học sinh: {name}")
        else:
            print("Không tìm thấy học sinh!")

    # Xem danh sách học sinh
    elif choice == "4":
        if students:
            print("\nDanh sách học sinh:")
            for i, student in enumerate(students, 1):
                print(f"{i}. {student}")
        else:
            print("Danh sách hiện đang trống!")

    # Thoát chương trình
    elif choice == "5":
        print("Chương trình kết thúc.")
        break

    # Lựa chọn không hợp lệ
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
