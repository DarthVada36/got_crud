# 🏰 Registro de Casas Nobles de Westeros

Este es un programa en **Python** que implementa un sistema **CRUD** (Crear, Leer, Actualizar y Eliminar) para gestionar **casas nobles** de Westeros, basado en **Game of Thrones**. Los datos se almacenan en un archivo `houses.json` para que se mantengan entre sesiones.

---

## 📌 ¿Qué es CRUD?
CRUD representa las cuatro operaciones básicas que podemos realizar en una base de datos:

- **Create (Crear)**: Agregar nuevas casas nobles a la lista.
- **Read (Leer)**: Mostrar todas las casas registradas.
- **Update (Actualizar)**: Modificar el lema de una casa existente.
- **Delete (Eliminar)**: Eliminar una casa de la lista.

---

## 🚀 Instalación y Ejecución
### **1️⃣ Requisitos Previos**
Para ejecutar este programa, necesitas tener **Python 3** instalado. Puedes verificarlo con:
```sh
python --version
```
Si no lo tienes, descárgalo desde [Python.org](https://www.python.org/downloads/).

### **2️⃣ Clonar o Descargar el Proyecto**
Puedes descargar este repositorio como archivo ZIP o clonarlo con:
```sh
git clone https://github.com/tu_usuario/registro-westeros.git
cd registro-westeros
```

### **3️⃣ Ejecutar el Programa**
Para iniciar el programa, usa el siguiente comando en la terminal:
```sh
python main.py
```

---

## 📜 Uso del Programa

Al ejecutar el programa, verás un menú como este:
```plaintext
🔹 Menú del Registro de Westeros 🔹
1️⃣ Ver casas
2️⃣ Agregar casa
3️⃣ Actualizar lema
4️⃣ Eliminar casa
5️⃣ Salir
```

### **🏰 Crear una Casa (Create - POST)**
Selecciona la opción `2` e ingresa los datos:
```plaintext
🏰 Ingresa el nombre de la nueva casa: Greyjoy
📜 Ingresa su lema: We Do Not Sow
✅ ¡La casa Greyjoy ha sido añadida con éxito!
```

### **📜 Ver Casas Registradas (Read - GET)**
Selecciona la opción `1` para listar todas las casas:
```plaintext
🏰 Casas Nobles de Westeros:
🔹 ID: 1 | Stark - Winter is Coming
🔹 ID: 2 | Lannister - Hear Me Roar
🔹 ID: 3 | Targaryen - Fire and Blood
🔹 ID: 4 | Greyjoy - We Do Not Sow
```

### **✍ Actualizar el Lema de una Casa (Update - PUT)**
Selecciona la opción `3` y proporciona el ID de la casa:
```plaintext
🔄 Ingresa el ID de la casa a modificar: 2
✍ Nuevo lema para Lannister: A Lannister Always Pays His Debts
✅ Lema actualizado con éxito.
```

### **🔥 Eliminar una Casa (Delete - DELETE)**
Selecciona la opción `4` y proporciona el ID de la casa a eliminar:
```plaintext
🔥 Ingresa el ID de la casa a eliminar: 3
💀 La casa ha caído en batalla.
```

---

## 🛠 ¿Cómo Funciona el JSON?
El programa guarda los datos en un archivo `houses.json`, que tiene esta estructura:
```json
[
    {"id": 1, "name": "Stark", "motto": "Winter is Coming"},
    {"id": 2, "name": "Lannister", "motto": "Hear Me Roar"},
    {"id": 3, "name": "Targaryen", "motto": "Fire and Blood"}
]
```
Cada vez que agregas, actualizas o eliminas una casa, el archivo JSON se actualiza automáticamente.

---

## 🎯 Reto Extra
1️⃣ **Prueba agregar la Casa Martell con el lema "Unbowed, Unbent, Unbroken"**.
2️⃣ **Abre `houses.json` y verifica cómo cambian los datos al hacer modificaciones**.
3️⃣ **Modifica el código para agregar un campo "soldiers" con la cantidad de tropas por casa**.

---

## 📜 Créditos
🔹 Desarrollado por **Vada Velázquez**
🔹 Inspirado en **Game of Thrones**

---

¡Que los Siete Reinos guíen tu código! 👑🔥

