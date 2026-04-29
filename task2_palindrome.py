from collections import deque
 
 
def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Нечутлива до регістру та пробілів.
    Використовує двосторонню чергу (deque).
    """
    # Очищаємо рядок від пробілів та переводимо в нижній регістр
    cleaned = text.replace(" ", "").lower()
 
    # Додаємо всі символи до двосторонньої черги
    char_deque = deque(cleaned)
 
    # Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
 
    return True
 
 
def main():
    print("=" * 50)
    print("      Перевірка рядка на паліндром")
    print("=" * 50)
 
    # Тестові приклади
    test_cases = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "Лівак з казкіл",
        "Python",
        "Абба",
        "level",
        "",
        "a",
    ]
 
    print("\n--- Автоматичне тестування ---")
    for test in test_cases:
        result = is_palindrome(test)
        status = "✅ Паліндром" if result else "❌ Не паліндром"
        print(f"  '{test}' → {status}")
 
    # Інтерактивний режим
    print("\n--- Введіть власний рядок ---")
    while True:
        user_input = input("\nВведіть рядок (або 'вихід' для завершення): ")
        if user_input.lower() in ("вихід", "exit", "quit"):
            print("До побачення!")
            break
        result = is_palindrome(user_input)
        if result:
            print(f"  ✅ '{user_input}' — це паліндром!")
        else:
            print(f"  ❌ '{user_input}' — не є паліндромом.")
 
 
if __name__ == "__main__":
    main()
