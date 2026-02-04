import { createRouter, createWebHistory } from 'vue-router'
import OperadorasPage from '../pages/OperadorasPage.vue'
import DetalheOperadoraPage from '../pages/DetalheOperadoraPage.vue'

const routes = [
  {
    path: '/',
    component: OperadorasPage
  },
  {
    path: '/operadora/:cnpj',
    component: DetalheOperadoraPage
  }
]

export default createRouter({
  history: createWebHistory(),
  routes
})