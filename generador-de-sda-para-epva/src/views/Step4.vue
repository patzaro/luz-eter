<template>
  <section>
    <h2>Descarga de la propuesta educativa</h2>

    <p>Puedes exportar la situación de aprendizaje como un documento PDF.</p>

    <button @click="exportarPDF">📄 Descargar PDF</button>
  </section>
</template>

<script setup>
import jsPDF from 'jspdf';
import { useSdaStore } from '../stores/sdaStore';

const sda = useSdaStore();

const exportarPDF = () => {
  const doc = new jsPDF();

  const contenido = `
  Situación de Aprendizaje para EPVA

  Saber básico: ${sda.datosFormulario.topic}
  Curso: ${sda.datosFormulario.course}
  Nº de sesiones: ${sda.datosFormulario.sessions}

  Contexto del grupo:
  ${sda.datosFormulario.context}

  Narrativa seleccionada:
  ${sda.narrativaElegida}

  Desarrollo completo:
  ${sda.desarrollo || 'Desarrollo no disponible'}
  `;

  doc.setFontSize(12);
  doc.text(contenido, 20, 20);
  doc.save('situacion-de-aprendizaje.pdf');
};
</script>

<style scoped>
section {
  max-width: 700px;
  margin: auto;
  padding: 2rem;
}
button {
  padding: 0.5rem 1rem;
  margin-top: 1rem;
}
</style>
