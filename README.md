# Download Speed Meter

Последовательно скачивает файл по указанному адресу, дожидаясь полного ответа. По успешным запросам показывает среднее время, общий объём и среднюю скорость. Неудачные попытки выводятся отдельно.

## Запуск

```bash
python3 app.py --url "https://example.com/image.jpg"
```

По умолчанию выполняется 10 запросов. Скорость и объём автоматически выводятся в подходящих единицах: B, KB, MB, GB или TB (1 KB = 1024 B).

## Параметры

- `--url URL` — адрес файла, обязателен.
  ```bash
  python3 app.py --url "https://example.com/image.jpg"
  ```
- `--try N` — число запросов, по умолчанию 10.
  ```bash
  python3 app.py --url "https://example.com/image.jpg" --try 3
  ```
- `--pure` — выводить объём в B, а скорость в B/s без перевода в KB/MB/GB; используйте для точности.
  ```bash
  python3 app.py --url "https://example.com/image.jpg" --pure
  ```
