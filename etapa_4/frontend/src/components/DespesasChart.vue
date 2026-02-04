<script setup>
import { ref, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'

import {
  Chart,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from 'chart.js'

import { buscarDespesasPorUF } from '../api/operadoras'

Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend)

const chartData = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {

    const dados = await buscarDespesasPorUF()

    chartData.value = {
      labels: dados.map(d => d.uf),
      datasets: [
        {
          label: 'Total de despesas por UF',
          data: dados.map(d => d.total)
        }
      ]
    }

  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="card">

    <h2>Distribuição de Despesas por UF</h2>

    <p v-if="loading">Carregando gráfico...</p>
    <p v-if="error">{{ error }}</p>

    <Bar v-if="chartData" :data="chartData" />

  </div>
</template>