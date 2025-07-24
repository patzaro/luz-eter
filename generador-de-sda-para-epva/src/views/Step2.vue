<template>
  <section>
    <h2>Selecciona una narrativa para continuar</h2>

    <div v-if="sda.narrativas.length === 0">
      <p>No hay narrativas generadas. ¿Volvemos al paso anterior?</p>
      <button @click="router.push('/')">Volver a inicio</button>
    </div>

    <div v-else>
      <ul>
        <li
          v-for="(narrativa, index) in sda.narrativas"
          :key="index"
          class="narrativa"
        >
          <label>
            <input
              type="radio"
              :value="narrativa"
              v-model="sda.narrativaElegida"
            />
            {{ narrativa }}
          </label>
        </li>
      </ul>

      <button
        @click="continuar"
        :disabled="!sda.narrativaElegida"
      >
        Continuar al desarrollo curricular
      </button>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useSdaStore } from '../stores/sdaStore';

const router = useRouter();
const sda = useSdaStore();

const continuar = () => {
  console.log('Narrativa seleccionada:', sda.narrativaElegida);
  router.push('/desarrollo'); // Redirige a Step3.vue
};
</script>

<style scoped>
section {
  max-width: 700px;
  margin: auto;
  padding: 2rem;
}
.narrativa {
  margin-bottom: 1rem;
  border-left: 3px solid #42b883;
  padding-left: 1rem;
}
button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
}
</style>
