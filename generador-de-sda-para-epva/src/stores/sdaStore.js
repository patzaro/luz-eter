import { defineStore } from 'pinia';

export const useSdaStore = defineStore('sda', {
  state: () => ({
  datosFormulario: { topic: '', course: '1º ESO', context: '', sessions: 5 },
  narrativas: [],
  narrativaElegida: '',
  desarrollo: ''
  })
});