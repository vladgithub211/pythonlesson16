prompt = "\nПривет! Меня зовут бот, я хочу узнать о тебе все:"
prompt += "\nВведите “out” для завершения программы"
prompt += "\n Введите ваше имя"
message = ""
while message != "out":
 	message = input(prompt)
 	print(f"Привет, круто что тебя {message}")

