choice = 1

while (choice != 3):
    print("\n--- NHẬP THÔNG TIN NHÂN VIÊN MỚI ---")
    employee_id = input("Nhập mã nhân viên: ").strip()
    employee_name = input("Nhập họ tên nhân viên: ").strip()
    department = input("Nhập tên phòng ban: ").strip()
    if employee_id == "":
        print("[CẢNH BÁO] Mã nhân viên không được để trống! Hủy bỏ hồ sơ.")
        continue
    if employee_name == "":
        print("[CẢNH BÁO] Họ tên nhân viên không được để trống! Hủy bỏ hồ sơ.")
        continue
    print("-----Phiếu Hồ Sơ Điện Tử-----")
    print(f"Mã Nhân Viên: {employee_id}")
    print(f"Họ và tên nhân viên: {employee_name}")
    print(f"Phòng ban đang công tác: {department if department != '' else 'Chưa xếp'}")
    print("-----------------------------")
    
    choice = int(input("Nhập số 3 để THOÁT hệ thống, hoặc bấm phím bất kỳ để TIẾP TỤC: "))

print("--- CHƯƠNG TRÌNH KẾT THÚC ---")