# 这是我们的条件判断语句

has_sunshine = True
is_good_mood = True

if True:
    print("今天是个好日子")


if False:
    print("此处不会被执行")
else:
    print("此处会被执行")

# if 晴天 and 心情好:
#     出门散步()
#
# if 晴天 or 心情好:
#     出门散步()

if True and False:
    print("此处不会被执行")

if True and True:
    print("此处会被执行")

if True or False:
    print("此处会被执行")

if False or True:
    print("此处会被执行")

if False or True and True:
    print("此处会被执行")

if False or False:
    print("此处不会被执行")



is_good_mood = True
if has_sunshine and is_good_mood:
    print("今天是个好日子")


has_sunshine = True
is_good_mood = False

if has_sunshine and is_good_mood:
    print("今天是个好日子")
else:
    print("今天不是个好日子")

if is_good_mood or has_sunshine:
    print("今天是个好日子")
else:
    print("今天不是个好日子")