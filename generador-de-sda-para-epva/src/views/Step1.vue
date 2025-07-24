<template>
  <section>
    <h1>Generador de SDA – Paso 1</h1>
    <form @submit.prevent="enviar">
      <label>
        Saber básico:
        <input v-model="sda.datosFormulario.topic" required />
      </label>

      <label>
        Curso:
        <select v-model="sda.datosFormulario.course">
          <option value="1º ESO">1º ESO</option>
          <option value="3º ESO">3º ESO</option>
        </select>
      </label>

      <label>
        Contexto del grupo (incluye medidas de atención a la diversidad si procede):
        <textarea v-model="sda.datosFormulario.context"></textarea>
      </label>

      <label>
        Nº de sesiones previstas:
        <input type="number" v-model="sda.datosFormulario.sessions" min="1" />
      </label>

      <button type="submit">Generar narrativas</button>
    </form>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useSdaStore } from '../stores/sdaStore';

const router = useRouter();
const sda = useSdaStore();

const enviar = async () => {
  const res = await fetch('/api/generar-narrativas', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(sda.datosFormulario)
  });

  const data = await res.json();
  sda.narrativas = data.narrativas;
  router.push('/narrativas');
};
</script>

<style scoped>
section {
  max-width: 700px;
  margin: auto;
  padding: 2rem;
}
label {
  display: block;
  margin-bottom: 1rem;
}
input,
select,
textarea {
  width: 100%;
  margin-top: 0.5rem;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
}
</style>
