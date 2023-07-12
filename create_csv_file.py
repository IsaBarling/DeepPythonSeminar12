import csv

def create_csv_file():
    fieldnames = ['Предмет']
    items = ['История', 'География', 'Английский', 'Музыка', 'Физкультура']

    with open('school_items.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow({'Предмет': item})

create_csv_file()
