from messages.main.consts import MAIN_EXIT, WRONG_INPUT
from messages.main.message_formatter import main_exception
from repository import TaskRepository
from service_layer import TaskService
from service_layer.service_helper import ServiceHelper
from storage import TaskStorage


def main() -> None:
    """
    Главный цикл приложения, который обрабатывает взаимодействие с пользователем и вызывает
    соответствующие методы у класса TaskService, выполняя основную бизнес логику
    """
    storage = TaskStorage()
    repository = TaskRepository(storage=storage)
    service_helper = ServiceHelper()
    service = TaskService(repository=repository, service_helper=service_helper)

    choices = {
        "1": service.show_tasks,
        "2": service.add_task,
        "3": service.update_task,
        "4": service.delete_task,
        "5": service.search_by_key_word,
        "6": lambda: print(MAIN_EXIT),
    }

    while True:
        choice = service.get_choice()
        choices.get(choice, lambda: print(WRONG_INPUT))()
        if choice == "6":
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(main_exception(exc=exc))
