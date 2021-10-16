from character_app import app
from flask import render_template, redirect, request  # Import Flask to allow us to create our app
from character_app.models.character import Character


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def home():
    characters = Character.get_all()
    return render_template(".html", characters=characters)


@app.route("/characters/add", methods=["POST"])
def add_character():
    Character.add(request.form)
    return redirect("/")

@app.route("/characters/<int:character_id>")
def show_character(character_id):
    data = {
        "id": character_id
    }
    character = Character.get_character_with_roles(data)
    return render_template("show_character.html", character=character)


@app.route("/characters/<int:character_id>/edit")
def edit_character(character_id):
    data = {
        "id": character_id
    }
    character = Character.get(data)
    return render_template("edit.html", character=character)

@app.route("/characters/<int:character_id>/update", methods=['POST'])
def update_character(character_id):
    Character.edit(request.form)
    return redirect(f"/characters/{character_id}/edit")

@app.route("/characters/<int:character_id>/delete")
def delete_character(character_id):
    data = {
        "id": character_id
    }
    character = Character.get(data)
    return render_template("delete.html", character=character)

@app.route("/characters/<int:character_id>/destroy", methods=["POST"])
def destroy_character(character_id):
    data = {
        "id": character_id
    }
    Character.delete(data)
    return redirect("/")

