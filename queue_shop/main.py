# Вантеев Руслан ИИАД_1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StoreQueue:
    def __init__(self):
        self.first = None
        self.last = None

    def join(self, name):
        person = Node(name)
        if not self.last:
            self.first = self.last = person
            print(f"{name} — первый в очереди!")
        else:
            self.last.next = person
            self.last = person
            print(f"{name} занял место за {self._prev_name(person)}.")

    def serve(self):
        if not self.first:
            print("Очередь пуста — некому обслуживать.")
            return None
        customer = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
            print(f"Обслужен последний покупатель: {customer}.")
        else:
            print(f"Обслужен: {customer}. Следующий: {self.first.data}")
        return customer

    def next_in_line(self):
        return self.first.data if self.first else "Никого нет"

    def _prev_name(self, new_node):
        current = self.first
        while current and current.next != new_node:
            current = current.next
        return current.data if current else "?"

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        print(f"[В начало] +{value}")

    def push_last(self, value):
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        print(f"[В конец] +{value}")

    def pop_first(self):
        if not self.head:
            print("Пусто — нечего удалять из начала.")
            return None
        item = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        print(f"[С начала] -{item}")
        return item

    def pop_last(self):
        if not self.tail:
            print("Пусто — нечего удалять из конца.")
            return None
        if self.head == self.tail:
            item = self.tail.data
            self.head = self.tail = None
            print(f"[С конца] -{item}")
            return item
        current = self.head
        while current.next != self.tail:
            current = current.next
        item = self.tail.data
        self.tail = current
        self.tail.next = None
        print(f"[С конца] -{item}")
        return item

    def peek_both(self):
        first = self.head.data if self.head else "—"
        last = self.tail.data if self.tail else "—"
        return f"Начало: {first} | Конец: {last}"

if __name__ == "__main__":
    print("СИСТЕМА ОБРАБОТКИ ЗАЯВОК (FIFO)")

    queue = StoreQueue()

    for order_id in ["Татьяна", "Алексей", "Владимир", "Николай"]:
        queue.join(order_id)

    print(f"\nСледующая заявка на выполнение: {queue.next_in_line()}")
    print("Начинаем обработку...\n")

    queue.serve()
    queue.serve()
    print(f"Теперь следующая: {queue.next_in_line()}")
    queue.serve()
    queue.serve()
    queue.serve()

    print("ДВУСТОРОННЯЯ ОЧЕРЕДЬ (Deque) — работа с приоритетами")


    dq = Deque()
    dq.push_first(10)
    dq.push_last(20)
    dq.push_first(5)
    dq.push_last(30)

    print(dq.peek_both())

    dq.pop_first()
    dq.pop_last()

    print(dq.peek_both())

    dq.pop_first()
    dq.pop_last()
    dq.pop_first()