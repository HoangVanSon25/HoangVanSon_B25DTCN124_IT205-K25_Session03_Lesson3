choice = 1

while (choice != 3):
    for i in range(1, 4):
        print(f"Nhập thông tin nhân viên thứ {i}")
        employee_id = input("Nhạp mã nhân viên: ").strip()
        employee_name = input("nhập họ tên nhân viên: ").strip()
        department = input("Nhập tên phòng ban: ").strip()
        
        if employee_id == "" or employee_name == "" or department =="":
            print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ hồ sơ cho nhân viên này.")
            continue
        
        print(f"-----Phiếu Hồ Sơ Điện Tử-----")
        print (f"Mã Nhân Viên: {employee_id}")
        print(f"Họ và tên nhân viên: {employee_name}")
        print(f"Phòng ban đang công tác: {department}")
    choice = int(input(f"Chọn 3 để thoát!"))
        
        
        
        