from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Dados da agenda telefônica de exemplo
phone_book = [
    {"name": "Alice", "phone": "123-456-7890"},
    {"name": "Bob", "phone": "234-567-8901"},
    {"name": "Charlie", "phone": "345-678-9012"},
    {"name": "David", "phone": "456-789-0123"},
    {"name": "Eve", "phone": "567-890-1234"},
]


def binary_search(contacts, name):
    low = 0
    high = len(contacts) - 1
    steps = []
    while low <= high:
        mid = (low + high) // 2
        step = {
            "low": low,
            "mid": mid,
            "high": high,
            "mid_name": contacts[mid]["name"],
            "compare": name,
        }
        steps.append(step)
        if contacts[mid]["name"] == name:
            return contacts[mid], steps
        elif contacts[mid]["name"] < name:
            low = mid + 1
        else:
            high = mid - 1
    return None, steps


def load_contacts_from_csv(filepath):
    contacts = []
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contacts.append({"name": row["nome"], "phone": row["telefone"]})
    return contacts


def save_contact_to_csv(filepath, contact):
    # Lê todos os contatos existentes
    contacts = load_contacts_from_csv(filepath)
    contacts.append(contact)
    # Ordena os contatos por nome
    contacts.sort(key=lambda x: x["name"])
    # Sobrescreve o CSV com todos os contatos ordenados
    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["nome", "telefone"])  # Cabeçalho
        for c in contacts:
            writer.writerow([c["name"], c["phone"]])


# Carrega contatos do CSV ao iniciar o app
phone_book = load_contacts_from_csv("flask-phonebook/contatos.csv")


@app.route("/", methods=["GET", "POST"])
def index():
    global phone_book
    add_message = None
    result = None
    steps = None
    if request.method == "POST":
        if "add_contact" in request.form:
            # Adiciona contato
            name = request.form["name"]
            phone = request.form["phone"]
            new_contact = {"name": name, "phone": phone}
            phone_book.append(new_contact)
            phone_book.sort(key=lambda x: x["name"])
            save_contact_to_csv("flask-phonebook/contatos.csv", new_contact)
            add_message = f"Contato '{name}' adicionado com sucesso!"
        elif "search_contact" in request.form:
            # Busca contato
            name = request.form["name"]
            result, steps = binary_search(phone_book, name)
    return render_template(
        "index.html",
        result=result,
        steps=steps,
        contacts=phone_book,
        add_message=add_message,
    )


if __name__ == "__main__":
    app.run(debug=True)
