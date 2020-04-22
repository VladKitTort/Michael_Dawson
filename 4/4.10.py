#Напишите проrрамму, которая бы считала по просьбе пользователя. Надо позволить пользователю ввести
#начапо и конец счета, а также интервал между называемыми целыми числами.

account_start = input("Напишите цифру с которой начинать счет:")
if account_start == "":
    account_start = int(0)
else:
    account_start = int(account_start)
end_account = input("Напишите цифру c которой кончается счет:")
if end_account == "":
    end_account = int(0)
else:
    end_account = int(end_account)
step = input("Можете указать шаг счета:")
if step == "":
    step = int(1)
else:
    step = int(step)
for i in range(account_start, end_account + 1, step):
    print(i)
