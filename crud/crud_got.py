import json
import os

# 📜 Nombre del archivo JSON donde guardaremos los datos
FILE_NAME = "houses.json"

# 📜 Cargar datos desde JSON si el archivo existe
def load_houses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# 📜 Guardar datos en JSON
def save_houses():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(houses, file, indent=4, ensure_ascii=False)

# 📜 Inicializar casas nobles
houses = load_houses()

# 📜 Mostrar todas las casas
def read_houses():
    print("\n🏰 Casas Nobles de Westeros:")
    if not houses:
        print("⚠ No hay casas registradas.")
        return
    for house in houses:
        print(f"🔹 ID: {house['id']} | {house['name']} - {house['motto']}")
    print("\n")

# 📜 Agregar una casa
def create_house():
    name = input("🏰 Ingresa el nombre de la nueva casa: ").strip()
    if not name:
        print("⚠ Error: El nombre no puede estar vacío.")
        return
    motto = input("📜 Ingresa su lema: ").strip()
    new_id = max((house["id"] for house in houses), default=0) + 1
    houses.append({"id": new_id, "name": name, "motto": motto})
    save_houses()
    print(f"✅ ¡La casa {name} ha sido añadida con éxito!")

# 📜 Actualizar lema de una casa
def update_house():
    house_id = int(input("🔄 Ingresa el ID de la casa a modificar: "))
    house = next((h for h in houses if h["id"] == house_id), None)
    if house:
        new_motto = input(f"✍ Nuevo lema para {house['name']}: ").strip()
        house["motto"] = new_motto
        save_houses()
        print("✅ Lema actualizado con éxito.")
    else:
        print("❌ Casa no encontrada.")

# 📜 Eliminar una casa
def delete_house():
    house_id = int(input("🔥 Ingresa el ID de la casa a eliminar: "))
    global houses
    houses = [house for house in houses if house["id"] != house_id]
    save_houses()
    print("💀 La casa ha caído en batalla.")

# 📜 Menú principal
def main():
    while True:
        print("\n🔹 Menú del Registro de Westeros 🔹")
        print("1️⃣ Ver casas")
        print("2️⃣ Agregar casa")
        print("3️⃣ Actualizar lema")
        print("4️⃣ Eliminar casa")
        print("5️⃣ Salir")

        choice = input("⚔ ¿Qué deseas hacer? (1-5): ")

        if choice == "1":
            read_houses()
        elif choice == "2":
            create_house()
        elif choice == "3":
            update_house()
        elif choice == "4":
            delete_house()
        elif choice == "5":
            print("👑 Fin del registro de Westeros. ¡Hasta la próxima!")
            break
        else:
            print("⚠ Opción no válida. Inténtalo de nuevo.")

# 📜 Ejecutar el programa
if __name__ == "__main__":
    main()
