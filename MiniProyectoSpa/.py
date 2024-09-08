// temporizador.js  

function obtenerHoraActual() {  
    const ahora = new Date();  
    return ahora.getHours() + ':' + ahora.getMinutes() + ':' + ahora.getSeconds();  
}  

function sumarTemporizador(temporal) {  
    const ahora = new Date();  
    const tiempoTotal = new Date(ahora.getTime() + temporal * 1000); // temporal en segundos  
    return tiempoTotal.getHours() + ':' + tiempoTotal.getMinutes() + ':' + tiempoTotal.getSeconds();  
}  

// Ejemplo de uso  
const tiempoTemporizador = 3600; // 1 hora en segundos  
console.log("Hora actual: " + obtenerHoraActual());  
console.log("Hora después de sumar el temporizador: " + sumarTemporizador(tiempoTemporizador));  