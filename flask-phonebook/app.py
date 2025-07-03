from flask import Flask, render_template, request, redirect, url_for

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
    while low <= high:
        mid = (low + high) // 2
        if contacts[mid]["name"] == name:
            return contacts[mid]
        elif contacts[mid]["name"] < name:
            low = mid + 1
        else:
            high = mid - 1
    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_contact():
    name = request.form["name"]
    phone = request.form["phone"]
    phone_book.append({"name": name, "phone": phone})
    phone_book.sort(
        key=lambda x: x["name"]
    )  # Mantém a lista ordenada para busca binária
    return redirect(url_for("index"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        name = request.form["name"]
        result = binary_search(phone_book, name)
        return render_template("search.html", result=result)
    return render_template("search.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)
