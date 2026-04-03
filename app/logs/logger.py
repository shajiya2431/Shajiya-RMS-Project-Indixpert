import datetime

class Logger:

    @staticmethod
    def log(message):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("app/logs/log.txt", "a", encoding="utf-8") as file:
            file.write(f"[{time}] {message}\n")