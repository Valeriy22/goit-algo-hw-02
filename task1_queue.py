import queue
import random
 
# Створити чергу заявок
requests_queue = queue.Queue()
request_counter = 0
 
 
def generate_request():
    """Генерує нову заявку та додає її до черги."""
    global request_counter
    request_counter += 1
    request_id = f"Заявка-{request_counter:03d}"
    requests_queue.put(request_id)
    print(f"[+] Додано: {request_id} | Заявок у черзі: {requests_queue.qsize()}")
 
 
def process_request():
    """Обробляє заявку, видаляючи її з черги."""
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"[✓] Оброблено: {request} | Залишилось у черзі: {requests_queue.qsize()}")
    else:
        print("[!] Черга порожня — немає заявок для обробки.")
 
 
def main():
    print("=" * 50)
    print("   Сервісний центр — Система обробки заявок")
    print("=" * 50)
 
    while True:
        print("\nМеню:")
        print("  1 — Додати нову заявку")
        print("  2 — Обробити заявку")
        print("  3 — Додати випадкову кількість заявок (1-5)")
        print("  4 — Показати кількість заявок у черзі")
        print("  0 — Вийти")
 
        choice = input("\nВаш вибір: ").strip()
 
        if choice == "1":
            generate_request()
        elif choice == "2":
            process_request()
        elif choice == "3":
            count = random.randint(1, 5)
            print(f"\nГенеруємо {count} заявок...")
            for _ in range(count):
                generate_request()
        elif choice == "4":
            print(f"\nУ черзі зараз: {requests_queue.qsize()} заявок.")
        elif choice == "0":
            print("\nЗавершення роботи сервісного центру. До побачення!")
            break
        else:
            print("[!] Невірний вибір. Спробуйте ще раз.")
 
 
if __name__ == "__main__":
    main()
