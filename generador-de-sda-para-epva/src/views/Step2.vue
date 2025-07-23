<template>
  <section>
    <h2>Selecciona una narrativa educativa</h2>

    <div v-if="loading">Cargando narrativas...</div>
    <ul v-else>
      <li v-for="(narrativa, index) in narrativas" :key="index">
        <label>
          <input
            type="radio"
            :value="narrativa"
            v-model="seleccionada"
          />
          {{ narrativa }}
        </label>
      </li>
    </ul>

    <button @click="continuar" :disabled="!seleccionada">
      Continuar al desarrollo curricular
    </button>
  </section>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'Step2',
  data() {
    return {
      narrativas: [],
      seleccionada: '',
      loading: true
    };
  },
  mounted() {
    // Puedes reemplazar esto con datos compartidos más adelante
    fetch('/api/generar-narrativas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        topic: 'El color como lenguaje',
        course: '1º ESO',
        context: 'Grupo con alta sensibilidad artística',
        diversity: 'Adaptaciones por TDAH',
        sessions: 6
      })
    })
      .then(res => res.json())
      .then(data => {
        this.narrativas = data.narrativas;
        this.loading = false;
      });
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    continuar() {
      console.log('Narrativa seleccionada:', this.seleccionada);
      this.router.push('/desarrollo');
    }
  }
};
</script>

