# ---- file: core/event_bus.py ----
from typing import Callable, Dict, List, Any

class EventBus:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventBus, cls).__new__(cls)
            cls._instance._subscribers: Dict[str, List[Callable[..., None]]] = {}
        return cls._instance

    def subscribe(self, event_name: str, callback: Callable[..., None]) -> None:
        """Mendaftarkan fungsi untuk mendengarkan event tertentu"""
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        if callback not in self._subscribers[event_name]:
            self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable[..., None]) -> None:
        """Menghapus fungsi dari daftar pendengar event"""
        if event_name in self._subscribers:
            if callback in self._subscribers[event_name]:
                self._subscribers[event_name].remove(callback)

    def publish(self, event_name: str, data: Any = None) -> None:
        """Mengirimkan event beserta datanya ke semua subscriber yang terdaftar"""
        if event_name in self._subscribers:
            for callback in self._subscribers[event_name]:
                try:
                    callback(data)
                except Exception as e:
                    print(f"Error handling event '{event_name}': {e}")

# Global instance yang bisa di-import dari mana saja
event_bus = EventBus()