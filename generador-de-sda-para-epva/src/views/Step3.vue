<template>
  <section>
    <h2>Desarrollo de la Situación de Aprendizaje</h2>

    <div v-if="loading">🧠 Generando desarrollo con IA...</div>

    <div v-else-if="desarrollo">
      <article class="desarrollo-box">
        <p v-for="(bloque, i) in desarrollo.split('\n\n')" :key="i">
          {{ bloque }}
        </p>
      </article>

      <button @click="router.push('/descarga')">
        Continuar a la descarga
      </button>
    </div>

    <div v-else>
      <p>No se pudo generar el desarrollo. Vuelve a elegir una narrativa.</p>
      <button @click="router.push('/narrativas')">Volver</button>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useSdaStore } from '../stores/sdaStore';

const router = useRouter();
const sda = useSdaStore();

const desarrollo = ref('');
const loading = ref(true);

onMounted(async () => {
  if (!sda.narrativaElegida) {
    loading.value = false;
    return;
  }

  const res = await fetch('/api/generar-desarrollo', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      narrativa: sda.narrativaElegida,
      curso: sda.datosFormulario.course,
      sesiones: sda.datosFormulario.sessions
    })
  });

  const data = await res.json();
  desarrollo.value = data.desarrollo; // string largo con el desarrollo
  sda.desarrollo = data.desarrollo;
  loading.value = false;
});
</script>

<style scoped>
section {
  max-width: 700px;
  margin: auto;
  padding: 2rem;
}
.desarrollo-box {
  border-left: 4px solid #42b883;
  padding-left: 1rem;
  white-space: pre-line;
  margin-bottom: 2rem;
}
button {
  padding: 0.5rem 1rem;
}
</style>
