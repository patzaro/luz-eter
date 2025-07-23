import { createRouter, createWebHistory } from 'vue-router';

import Step1 from '../views/Step1.vue';
import Step2 from '../views/Step2.vue';
import Step3 from '../views/Step3.vue';
import Step4 from '../views/Step4.vue';

const routes = [
  { path: '/', component: Step1 },
  { path: '/narrativas', component: Step2 },
  { path: '/desarrollo', component: Step3 },
  { path: '/descarga', component: Step4 }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;