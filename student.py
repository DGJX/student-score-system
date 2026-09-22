
def input_student_id():
    print("=====学号录入模块=====")
    while True:
        stu_id = input("请输入学生学号：").strip()
        if not stu_id:
            print("提示：学号不能为空！")
        elif not stu_id.isdigit():
            print("提示：学号只能是数字！")
        else:
            print(f"✅录入成功，学生学号：{stu_id}")
            return stu_id


if __name__ == "__main__":
    input_student_id()