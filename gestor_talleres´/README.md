# 🎓 Gestor de Talleres de Formación Profesional

## 📌 Descripción del proyecto

Este proyecto consiste en una **aplicación web para la gestión de talleres de formación profesional**, permitiendo a estudiantes y administradores interactuar con talleres como cursos técnicos, capacitaciones prácticas y programas de actualización.

La aplicación está compuesta por un **backend con Flask (API RESTful)** y un **frontend con HTML, CSS, JavaScript y Bootstrap**.

---

## 🛠️ Tecnologías utilizadas

### Backend

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-CORS
* SQLite (base de datos)

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Control de versiones

* Git
* GitHub

---

## 📁 Estructura del proyecto

```
gestor_talleres/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
└── README.md
```

---

## 🚀 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/gestor_talleres.git
cd gestor_talleres
```

### 2️⃣ Instalar dependencias

```bash
pip install flask flask-sqlalchemy flask-cors
```

### 3️⃣ Ejecutar el backend

```bash
cd backend
python app.py
```

El servidor se ejecutará en:

```
http://127.0.0.1:5000
```

### 4️⃣ Ejecutar el frontend

Abrir el archivo:

```
frontend/index.html
```

En el navegador o con **Live Server**.

---

## 🔹 API RESTful

### 📌 Endpoints disponibles

| Método | Endpoint                 | Descripción                  |
| ------ | ------------------------ | ---------------------------- |
| GET    | /workshops               | Obtener todos los talleres   |
| GET    | /workshops/{id}          | Obtener un taller específico |
| POST   | /workshops               | Crear un taller              |
| PUT    | /workshops/{id}          | Modificar un taller          |
| DELETE | /workshops/{id}          | Eliminar un taller           |
| POST   | /workshops/{id}/register | Registrar estudiante         |

Todas las respuestas se devuelven en formato **JSON** y utilizan códigos de estado HTTP apropiados.

---

## 🧑‍🎓 Funcionalidades

### Estudiantes

* Visualizar talleres disponibles
* Registrarse a un taller

### Administradores

* Crear talleres
* Modificar talleres
* Cancelar (eliminar) talleres

---

## 🗄️ Base de datos

La base de datos utiliza **SQLite**, almacenando la información en un archivo local.

### Tablas principales:

* **Workshop**: información de los talleres
* **Registration**: estudiantes registrados por taller

---

## 🧪 Pruebas

Los endpoints pueden ser probados mediante:

* Navegador
* Thunder Client (VS Code)
* Postman (opcional)

---

## 📚 Conclusión

Este proyecto demuestra la implementación de una aplicación web completa utilizando una arquitectura cliente-servidor, aplicando principios de APIs REST, bases de datos relacionales y desarrollo frontend.

---

## ✍️ Autor

Proyecto académico – Universidad Interamericana de Panamá
