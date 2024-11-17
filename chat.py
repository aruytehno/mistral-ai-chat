from mistralai import Mistral
from decouple import config

# Установите токен API
api_key = config('MISTRAL_API_KEY', default=None)

if not api_key:
    raise ValueError("API ключ не найден. Проверьте файл .env или переменные окружения.")

# Название модели
model = "mistral-large-latest"

# Инициализация клиента
client = Mistral(api_key=api_key)

def main():
    print("=" * 50)
    print("Добро пожаловать в консольный чат с Mistral AI!")
    print("Команды:")
    print(" - 'exit' для выхода из чата")
    print(" - 'clear' для очистки контекста")
    print("=" * 50)

    # Начальный контекст диалога
    context = []

    while True:
        # Получение пользовательского ввода
        user_input = input("\nВы: ").strip()

        # Обработка команд
        if user_input.lower() == "exit":
            print("Чат завершен. Спасибо за использование!")
            break
        elif user_input.lower() == "clear":
            context = []
            print("Контекст очищен.")
            continue

        # Добавление пользовательского сообщения в контекст
        context.append({"role": "user", "content": user_input})

        try:
            # Отправка запроса к модели
            chat_response = client.chat.complete(
                model=model,
                messages=context
            )

            # Получение ответа модели
            ai_message = chat_response.choices[0].message.content
            print(f"Mistral: {ai_message}")

            # Добавление ответа модели в контекст
            context.append({"role": "assistant", "content": ai_message})
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break

if __name__ == "__main__":
    main()
