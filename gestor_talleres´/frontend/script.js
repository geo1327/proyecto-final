fetch('http://localhost:5000/workshops')
.then(res => res.json())
.then(data => {
const tabla = document.getElementById('tabla');
data.forEach(w => {
tabla.innerHTML += `<tr><td>${w.nombre}</td><td>${w.fecha}</td></tr>`;
});
});